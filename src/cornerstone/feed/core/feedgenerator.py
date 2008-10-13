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

import operator
import types
from sets import Set
from elementtreewriter.xmlwriter import XMLWriter
from zope.component import queryUtility
from zope.component import getAdapters
from interfaces import IFeed
from interfaces import IFeedSkeletonProducer
from interfaces import IFeedModifier
from interfaces import IMimeTypeLookup
from interfaces import INamespacePrefix

class FeedGenerator(object):
    
    def __init__(self, feed, name):
        assert(IFeed.providedBy(feed))
        self.feed = feed
        self.name = name
        
    def generate(self):
        """the rendered feed.
        
        @return: tuple of data and mimetype.
        """
        producer = queryUtility(IFeedSkeletonProducer, name=self.name)
        if producer is None:
            return None, None
        tree = producer()        
        named_modifiers = list(getAdapters((self.feed, tree), IFeedModifier))
        named_modifiers.sort(key=operator.itemgetter(0))
        namespaces = Set()        
        for name, modifier in named_modifiers:
            ns = modifier.modify()
            namespaces.update(ns)
        mimetype = IMimeTypeLookup(tree)
        prefixmap = {}
        for ns in namespaces:
            prefix = queryUtility(INamespacePrefix, name=ns)
            if prefix is None:
                continue
            prefixmap[ns] = prefix
        writer = XMLWriter(tree, prefixmap)
        result = writer(), mimetype
        return result
                
    def __call__(self):    
        return self.generate()
    
    
    