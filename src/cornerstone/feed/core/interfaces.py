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
# This definition was initially taken from Products.basesyndication. Thanks to
# Tim Hicks and all contributors for the ideas. Finally theres not much left
# from the original code

__author__ = """Jens Klein <jens@bluedynamics.com>"""
__docformat__ = 'plain'

from zope.interface import Interface
from zope.interface import Attribute


class IFeedEntry(Interface):
    """A single syndication feed entry.
    """    
    title = Attribute("Title of this entry.")
    description = Attribute("Short description of this entry.")
    webURL = Attribute("URL for the web view of this IFeedEntry.")
    contents = Attribute("List of dicts with keys: body, mimetype, src(url).")
    uid = Attribute("Unique ID for this entry. This UID should never change.")
    author = Attribute("Author of this entry.")
    effectiveDate = Attribute("The datetime this entry was first published.")
    modifiedDate = Attribute("The datetime this entry was last modified.")
    tags = Attribute("tags/keywords/subjects associated with this entry. "
                     "list or tuple.")
    rights = Attribute("The dublin core 'rights' associated with this entry.")
    enclosures = Attribute("One or more IEnclosure instances or None.")

class IFeed(Interface):
    """A syndication feed aggregating one or more IFeedEntryFactory
    """
    uid = Attribute("Unique ID for this feed.")
    feedURL = Attribute("Direct URL to the feed.")
    baseURL = Attribute("Used for supporting relative URLs in feeds.")
    imageURL = Attribute("URL of an image that can be embedded in feeds.")
    iconURL = Attribute("URL of an icon that can be embedded in feeds.")
    webURL = Attribute("URL for the web view of this feed.")
    encoding = Attribute("Character encoding for the feed.")
    title = Attribute("Title of this feed.")
    description = Attribute("Description of the feed.")
    author = Attribute("Author of this feed.")
    rights = Attribute("The dublin core 'rights' associated with this feed.")
    generator = Attribute("Software generating the feed")
    modifiedDate = Attribute("The datetime this feed was last modified. ")
    updatePeriod = Attribute("??")
    updateFrequency = Attribute("??")    
    max = Attribute("maximum number of entries to include, zero means all.")
    factories = Attribute("Sequence of IFeedEntryFactories objects.")

    def getFeedEntries(limit=True):
        """sorted sequence of IFeedEntry objects to build a feed with.

        Sorting based on publication datetime, newest first.
        
        @param limit: limit to 'max' entries
        """    

class IEnclosure(Interface):
    """Represents an 'enclosed' file that is explicitly linked to within
    an IFeedEntry.

    This is here to support podcasting.
    """

    url = Attribute("URL of the enclosed file.")
    major = Attribute("major mime-type of the enclosed file.")
    minor = Attribute("minor mime-type of the enclosed file.")
    mimetype = Attribute("full mime-type of the enclosed file.")

    def __len__():
       """size/length of the enclosed file in bytes."""       

class IFeedEntryFactory(Interface):
    """A single source of IFeedEntry objects for a feed.
    """

    def __iter__():
        """A sequence of IFeedEntry objects.
        """
        
################################################################################

class IFeedSkeleton(Interface):
    """marker for elementree."""

class IFeedEntrySkeleton(Interface):
    """marker for elementree node"""

class IFeedSkeletonProducer(Interface):
    """Factory for a feed skeleton (ElementTree)"""

class IFeedEntrySkeletonProducer(Interface):
    """Factory for a feed entry skeleton (ElementTree)"""
    
        
class IFeedEntryModifier(Interface):
    """Modifies the feed entry node."""
    
    def modify():
        """does the modification."""      
        

class IFeedModifier(Interface):
    """Modifies the feed tree. Fetches and calls."""
    
    def modify():
        """does the modification."""
        
class IFeedEntryModifier(Interface):
    """Modifies the feed entry node."""
    
    def modify():
        """does the modification."""      
        
class IMimeTypeLookup(Interface):
    """return a mimetype as string."""
    
class INamespacePrefix(Interface):
    """return a string as prefix for the namespace."""
        