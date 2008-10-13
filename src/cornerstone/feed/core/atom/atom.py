#
# Copyright 2008, BlueDynamics Alliance, Austria - http://bluedynamics.com
#
# Zope Public License (ZPL)
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL). A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
__author__ = """Jens Klein <jens@bluedynamics.com>"""
__docformat__ = 'plain'

import os    
from zope.interface import implementer
from zope.interface import implements
from zope.interface import alsoProvides
from cornerstone.feed.core.interfaces import IFeedSkeletonProducer
from interfaces import IAtomFeedSkeleton
from interfaces import IAtomFeedEntrySkeleton
from interfaces import IAtomFeedEntrySkeletonProducer
from elementtree.ElementTree import parse
try:
    from cElementTree import Element as cElement    
    class Element(cElement):
        """Make wrapped Element, enables usage in CA."""
except:
    from elementtree.ElementTree import Element
    

def AtomNamespacePrefix():
    return ''

def XMLNamespacePrefix():
    return 'xml'
    
def XHTMLNamespacePrefix():
    return 'xhtml'
    
class FeedSkelFactory(object):
    implements(IFeedSkeletonProducer)
    
    def __call__(self):
        file = open(os.path.join(os.path.dirname(__file__), 'atom.xml'))
        et = parse(file)
        file.close()
        et 
        alsoProvides(et, IAtomFeedSkeleton)
        return et

class EntrySkelFactory(object):
    implements(IAtomFeedEntrySkeletonProducer)
    
    def __call__(self):
        el = Element("{http://www.w3.org/2005/Atom}entry")
        el.tail = '\n'
        alsoProvides(el, IAtomFeedEntrySkeleton)
        return el
    
