#
# Copyright 2008, BlueDynamics Alliance, Austria - http://bluedynamics.com
#
# GNU General Public Licence Version 2 or later - see LICENCE.GPL

__author__ = """Jens Klein <jens@bluedynamics.com>"""
__docformat__ = 'plain'

import cgi
try:
    from celementtree.ElementTree import Element
except ImportError:
    from elementtree.ElementTree import Element
from cornerstone.feed.core.utils import iso8601

xhtmlns = 'http://www.w3.org/1999/xhtml'

def applyAtomText(node, text):
    """Text according to RFC4248 Section 3.1"""
    if isinstance(text, str):
        node.text = cgi.escape(text)
    elif isinstance(text, dict):
        content = text['text']
        type = text.get('type', 'text')
        assert type in ('text', 'html', 'xhtml')
        node.attrib['type'] = type
        if type == 'xhtml':
            div = Element("{%s}div" % xhtmlns)
            div.text = text['text'] # TODO: Do we need to add parsed nodes?
            node.append(div)
        else:
            node.text = cgi.escape(text['text'])                
    else:
        raise ValueError, "text must be string or dict."

    
def applyAtomPerson(node, person):
    if isinstance(person, str):
        node.text = cgi.escape(person)
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