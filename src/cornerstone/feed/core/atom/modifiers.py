# Copyright 2008-2009, BlueDynamics Alliance - http://bluedynamics.com
# Zope Public License (ZPL)

import operator
import cgi
from sets import Set
from zope.interface import implements
from zope.component import getUtility
from zope.component import getAdapters
from cornerstone.feed.core.interfaces import IFeedModifier
from cornerstone.feed.core.interfaces import IFeedEntryModifier
from interfaces import IAtomFeedEntrySkeletonProducer
from utils import applyAtomText
from utils import applyAtomPerson
from utils import applyAtomDate
from utils import createLink
from utils import xhtmlns

try:
    from cElementTree import Element as cElement    
    class Element(cElement):
        """Make wrapped Element, enables usage in CA."""
except:
    from elementtree.ElementTree import Element
    
xmlns = "http://www.w3.org/XML/1998/namespace"

class AtomModifierBase(object):
    
    def modifyMetadata(self, obj, node):
        # author element RFC4248 Section 4.2.1
        if obj.author:
            if isinstance(obj.author, list) or \
               isinstance(obj.author, tuple):
                authors = list(obj.author)
            elif isinstance(obj.author, str) or \
                 isinstance(obj.author, dict):
                authors = [obj.author]
            else:
                raise ValueError, 'author must be string|dict or tuple|list of'\
                                  ' string|dict or None.'
            for author in authors:
                el = Element(self.namespace+'author')
                applyAtomPerson(el, author)
                node.append(el) 

        # category element RFC4248 Section 4.2.2
        # TODO

        # contributor element RFC4248 Section 4.2.3
        # TODO

        # generator element RFC4248 Section 4.2.4
        # only valid for feed, not for entry, see specific implementation
        
        # icon element RFC4248 Section 4.2.5        
        # not general valid, must be handled individual
        
        # id element RFC4248 Section 4.2.6
        el = Element(self.namespace+'id')
        el.text = obj.uid
        node.append(el)

        # link elements RFC4248 Section 4.2.7 
        # MUST be handled individual!
        
        # logo element RFC4248 Section 4.2.8
        # MUST be handled individual!
            
        # published element RFC4248 Section 4.2.9
        # TODO

        # rights element RFC4248 Section 4.2.10
        if obj.rights:
            el = Element(self.namespace+'rights')
            applyAtomText(el, obj.rights)
            node.append(el)

        # source element RFC4248 Section 4.2.11
        # TODO
        
        # subtitle element RFC4248 Section 4.2.12
        # TODO

        # summary element RFC4248 Section 4.2.13        
        if obj.description:
            el = Element(self.namespace+'summary')
            applyAtomText(el, obj.description)
            node.append(el)
            
        # title element RFC4248 Section 4.2.14
        el = Element(self.namespace+'title')
        applyAtomText(el, obj.title)
        node.append(el)
        
        # updated element RFC4248 Section 4.2.15
        el = Element(self.namespace+'updated')
        applyAtomDate(el, obj.modifiedDate)      
        node.append(el)

class AtomFeedModifier(AtomModifierBase):
    implements(IFeedModifier)
    
    namespace = "{http://www.w3.org/2005/Atom}"
    
    def __init__(self, feed, tree):
        self.feed = feed
        self.tree = tree
        
    def modify(self):
        assert self.feed.feedURL, 'feedURL must be provided' 
        assert self.feed.webURL, 'webURL must be provided'
        assert self.feed.baseURL, 'baseURL must be provided'
        assert self.feed.uid, 'uid must be provided' 

        ####################################
        # feed element RFC4248 Section 4.1.1
        root = self.tree.getroot()
        root.attrib['{%s}base' % xmlns] = self.feed.baseURL

        #####################################
        # entry element RFC4248 Section 4.1.2
        producer = getUtility(IAtomFeedEntrySkeletonProducer)
        namespaces = Set([self.namespace, xmlns])
        for entry in self.feed.getFeedEntries():
            node = producer()
            named_modifiers = list(getAdapters((entry, node), 
                                               IFeedEntryModifier))
            named_modifiers.sort(key=operator.itemgetter(0))
            for name, modifier in named_modifiers:
                ns = modifier.modify()
                namespaces.update(ns)
            root.append(node)
        self.modifyMetadata(self.feed, root)    

        #########################################
        # generator element RFC4248 Section 4.2.4
        gen = self.feed.generator
        assert(isinstance(gen, dict), 'generator is provided, but not a '
                                      'dict instance')
        el = Element(self.namespace+'generator')
        el.text = cgi.escape(gen.get('text', 'cornerstone.feed'))
        if gen.get('uri', None):
            el.attrib['uri'] = gen.get('uri')
        if gen.get('version', None):
            el.attrib['version'] = gen.get('version')
        root.append(el)

        # icon element RFC4248 Section 4.2.5        
        if self.feed.iconURL:
            el = Element(self.namespace+'icon')
            el.text = self.feed.iconURL
            root.append(el)

        # link elements RFC4248 Section 4.2.7
        if self.feed.feedURL:
            root.append(createLink(self.feed.feedURL, 'self'))

        if self.feed.webURL:
            root.append(createLink(self.feed.feedURL, 'alternate'))                    

        # logo element RFC4248 Section 4.2.8
        if self.feed.imageURL:
            el = Element(self.namespace+'logo')
            el.text = self.feed.imageURL
            root.append(el) 
        return namespaces
    
class AtomFeedEntryModifier(AtomModifierBase):
    implements(IFeedEntryModifier)

    namespace = "{http://www.w3.org/2005/Atom}"
    
    def __init__(self, entry, node):
        self.entry = entry
        self.node = node
        
    def modify(self):
        # self.node is an atom entry, see RFC4248 Section 4.1.2
        
        ########################################
        # content elements RFC4248 Section 4.1.3
        contents = self.entry.contents
        if not (isinstance(contents, list) or isinstance(contents, tuple)):
            contents = [contents]
        for content in contents:
            el = Element(self.namespace+"content")
            # see RFC4248 Section 4.1.3.1 to 4.1.3.3
            if content.get('body', None):         
                type = content.get('type', 'text')       
                if 'xhtml' in type:
                    el.attrib['type'] = 'xhtml'
                    applyAtomText(el, {'text':content.get('body'),
                                       'type': 'xhtml'})
                elif 'html' in type:
                    el.attrib['type'] = 'html'
                    applyAtomText(el, {'text':content.get('body'),
                                       'type': 'html'})
                elif '/plain' in type or type=='text':
                    el.attrib['type'] = 'text'
                    applyAtomText(el, {'text':content.get('body'),
                                       'type': 'text'})
                elif type.endswith('+xml') or type.endswith('/xml'):
                    el.attrib['type'] = type
                    el.text = content.get('body')
                else: # base64 encode body                    
                    el.attrib['type'] = type
                    raise NotImplementedError, 'TODO: support base64.' 
            elif content.get('src', None):
                type = content.get('type', 'application/octet-stream')
                el.attrib['type'] = type
                el.attrib['src'] = content.get('src')
            self.node.append(el)
        
        #######################################
        # metadata elements RFC4248 Section 4.2
        self.modifyMetadata(self.entry, self.node)

        # link elements RFC4248 Section 4.2.7
        if self.entry.webURL:
            self.node.append(createLink(self.entry.webURL, 'alternate'))
        
        # handle enclosures RFC4248 Section 4.2.7.2. The "rel" Attribute
        if self.entry.enclosures:
            for enclosure in self.entry.enclosures:
                el = Element(self.namespace+"link")
                el.attrib['rel'] = 'enclosure'
                el.attrib['type'] = enclosure.mimetype
                el.attrib['length'] = str(len(enclosure))
                el.attrib['href'] = enclosure.url
                self.node.append(el)
        
        return [self.namespace, xhtmlns]        