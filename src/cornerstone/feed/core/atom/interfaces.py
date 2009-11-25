# Copyright 2008-2009, BlueDynamics Alliance - http://bluedynamics.com
# Zope Public License (ZPL)

from cornerstone.feed.core.interfaces import IFeedSkeleton
from cornerstone.feed.core.interfaces import IFeedEntrySkeleton
from cornerstone.feed.core.interfaces import IFeedEntrySkeletonProducer

class IAtomFeedSkeleton(IFeedSkeleton):
    """Marker for atom feed elementree.
    """

class IAtomFeedEntrySkeleton(IFeedEntrySkeleton):
    """Marker for atom entry elementree node.
    """

class IAtomFeedEntrySkeletonProducer(IFeedEntrySkeletonProducer):
    """Factory for one atom feed entry.
    """