from datetime import datetime
from zope.interface import implements
from cornerstone.feed.core.interfaces import IFeed
from cornerstone.feed.core.interfaces import IFeedEntry

class FeedDummy(object):
    implements(IFeed)
    
    def __init__(self, *args, **kwargs):
        self.uid = kwargs.get('uid', "12345")
        self.feedURL = kwargs.get('baseURL', "http://localhost/++feed++/atom.xml")
        self.baseURL = kwargs.get('baseURL', "http://localhost/")
        self.imageURL = kwargs.get('imageURL', "http://localhost/image.png")
        self.iconURL = kwargs.get('imageURL', "http://localhost/icon.png")
        self.webURL = kwargs.get('webURL', "http://localhost/www")
        self.encoding = kwargs.get("encoding", "utf8")
        self.title = kwargs.get('title', "Title of this feed.")
        self.description = kwargs.get('description', "Description of the feed.")
        self.author = kwargs.get('author', "Author(s) of the feed.")
        self.generator = kwargs.get('generator', {'text': "cornerstone.feed testing"})
        self.rights = kwargs.get('rights', "GPLv2")        
        self.updatePeriod = kwargs.get('updatePeriod', 1)
        self.updateFrequency = kwargs.get('updateFrequency', 0)
        self.max = kwargs.get('max', 0)
        self.modifiedDate = kwargs.get('modifiedDate', 
                                       datetime(2008, 8, 8, 8, 8, 8))

    @property
    def factories(self):
        return []

    def getFeedEntries(self, max_only=True):
        """sorted sequence of IFeedEntry objects with which to build a feed.

        Sorting based on publication datetime, newest first.
        """ 
        res = []   
        for idx in range(0, 3):
            res.append(FeedEntryDummy(uid=str(idx)))
        return res
    
dummyContents = [
    {"body": 'body text<br />'*3, 'mimetype': 'text/html'},
    {'mimetype': 'text/xhtml', 'src':'http://localhost/body'},
]    
    
class FeedEntryDummy(object):
    implements(IFeedEntry)
        
    def __init__(self, *args, **kwargs):
        self.uid = kwargs.get('uid')
        self.title = kwargs.get('title', "Entry #%s" % self.uid)
        self.description = kwargs.get('description', "Short description of this entry.")
        self.webURL = kwargs.get('webURL', "URL for the web view of this IFeedEntry.")
        self.contents = kwargs.get('contents', dummyContents)
        self.xhtml = kwargs.get('xhtml', "xhtml body content of this entry, or None")
        self.author = kwargs.get('author', "Jens Klein.")
        self.effectiveDate = kwargs.get('effectiveDate', "The datetime this entry was first published.")
        self.modifiedDate = kwargs.get('modifedDate', "The datetime this entry was last modified.")
        self.tags = kwargs.get('tags', ['test', 'case'])
        self.rights = kwargs.get('rights', "GPL")
        self.enclosure = None

def makeFeedDummy(*args, **kwargs):
    return FeedDummy(*args, **kwargs)
