from plone.indexer.decorator import indexer
from Products.CSCS.CSCSEvent import CSCSEvent
from DateTime import DateTime

@indexer(CSCSEvent)
def cscsevent_start(obj):
    if obj.start_date:
        return DateTime(obj.start_date)

@indexer(CSCSEvent)
def cscsevent_end(obj):
    if obj.end_date:
        return DateTime(obj.end_date)
