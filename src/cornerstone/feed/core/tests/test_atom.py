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
    suite = doctest.DocFileSuite('modifiers.txt',
                     package='cornerstone.feed.core.atom',
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
