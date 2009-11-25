# Copyright 2008-2009, BlueDynamics Alliance - http://bluedynamics.com
# Zope Public License (ZPL)

from zope.interface import implementer
from zope.component import adapter
from cornerstone.feed.core.interfaces import IMimeTypeLookup
from interfaces import IAtomFeedSkeleton

@adapter(IAtomFeedSkeleton)
@implementer(IMimeTypeLookup)
def atomMimeTypeLookup(context):
    return "application/atom+xml"