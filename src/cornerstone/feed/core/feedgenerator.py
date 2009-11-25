# Copyright 2008-2009, BlueDynamics Alliance - http://bluedynamics.com
# Zope Public License (ZPL)

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
    
    
    