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

from datetime import datetime
try:
    # allow to use with or without zope2
    from DateTime import DateTime
except:
    DateTime = classobj('DateTime', object, {})
    
def iso8601(dt):    
    if isinstance(dt, DateTime):
        return DateTime.ISO8601()
    if isinstance(dt, datetime):
        return dt.isoformat()
    if isinstance(dt, str):
        return dt
    raise ValueError, "need some date/time or a string here"



    
    