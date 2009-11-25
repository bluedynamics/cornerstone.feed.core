# Copyright 2008-2009, BlueDynamics Alliance - http://bluedynamics.com
# Zope Public License (ZPL)

import unittest
from pprint import pprint
from zope.testing import doctest
from zope.testing.cleanup import cleanUp
from zope.app.testing import placelesssetup
from zope.app.component.hooks import setHooks
from Products.Five import zcml
from interact import interact
from common import makeFeedDummy

class AtomLayer:

    @classmethod
    def testSetUp(cls):
        import zope.component
        zcml.load_config('meta.zcml', zope.component)
        import cornerstone.feed.core.atom
        zcml.load_config('configure.zcml', cornerstone.feed.core.atom)
        setHooks()

    @classmethod
    def testTearDown(cls):
        cleanUp()

def test_suite():
    suite = doctest.DocFileSuite('feedgenerator.txt',
                     package='cornerstone.feed.core',
                     tearDown=placelesssetup.tearDown,
                     optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS,
                     globs={'interact': interact,
                            'pprint': pprint,
                            'makeFeedDummy': makeFeedDummy}                     
                     )
    suite.layer = AtomLayer
    return unittest.TestSuite((suite,))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
