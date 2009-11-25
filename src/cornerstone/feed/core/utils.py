# Copyright 2008-2009, BlueDynamics Alliance - http://bluedynamics.com
# Zope Public License (ZPL)

from datetime import datetime
try:
    # allow to use with or without zope2
    from DateTime import DateTime
except:
    DateTime = classobj('DateTime', object, {})
    
def iso8601(dt):  
    if isinstance(dt, DateTime):
        return DateTime.ISO8601(dt)
    if isinstance(dt, datetime):
        return dt.isoformat()
    if isinstance(dt, str):
        return dt
    raise ValueError, "need some date/time or a string here"