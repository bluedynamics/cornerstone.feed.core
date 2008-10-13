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

from cornerstone.feed.core.interfaces import IFeedSkeleton
from cornerstone.feed.core.interfaces import IFeedEntrySkeleton
from cornerstone.feed.core.interfaces import IFeedEntrySkeletonProducer

class IAtomFeedSkeleton(IFeedSkeleton):
    """marker for atom feed elementree."""

class IAtomFeedEntrySkeleton(IFeedEntrySkeleton):
    """marker for atom entry elementree node"""

class IAtomFeedEntrySkeletonProducer(IFeedEntrySkeletonProducer):
    """factory for one atom feed entry"""
    
