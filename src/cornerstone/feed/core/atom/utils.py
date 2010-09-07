# Copyright 2008-2009, BlueDynamics Alliance - http://bluedynamics.com
# Zope Public License (ZPL)

import cgi
try:
    from celementtree.ElementTree import Element
except ImportError:
    from elementtree.ElementTree import Element
from elementtree.ElementTree import fromstring
from cornerstone.feed.core.utils import iso8601

xhtmlns = 'http://www.w3.org/1999/xhtml'

def applyAtomText(node, text):
    """Text according to RFC4248 Section 3.1.
    """
    if isinstance(text, str):
        node.text = cgi.escape(text)
    elif isinstance(text, dict):
        content = text['text']
        type = text.get('type', 'text')
        assert type in ('text', 'html', 'xhtml')
        node.attrib['type'] = type
        if type == 'xhtml':
            body = '<div xmlns="http://www.w3.org/1999/xhtml">%s</div>'
            body = body % text['text']
            # TODO: try catch around, and if not xml fallback to html
            try:
                body = fromstring(body.encode('utf-8'))
            except Exception, e:
                print body
                body = fromstring(
                            '<p>Invalid XHTML Content. Could not render.</p>')
            node.append(body)
        else:
            node.text = cgi.escape(text['text'])                
    else:
        raise ValueError, "text must be string or dict."

def applyAtomPerson(node, person):
    if isinstance(person, str):
        name = Element('{http://www.w3.org/2005/Atom}name')
        name.text = cgi.escape(person)
        node.append(name)
    elif isinstance(info, dict):
        raise NotImplementedError, 'TODO: support it.'

def applyAtomDate(node, dt):
    node.text = iso8601(dt)
    
def createLink(link, rel=None):
    node = Element('{http://www.w3.org/2005/Atom}link')
    if isinstance(link, str) and rel is not None:
        node.attrib['href'] = cgi.escape(link)
        node.attrib['rel'] = rel
        return node
    elif isinstance(info, dict):
        raise NotImplementedError, 'TODO: support it.'    
    else:
        raise ValueError, \
              "link must be string or dict and if its string rel must be given."