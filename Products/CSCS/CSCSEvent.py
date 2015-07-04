from Products.Archetypes.public import *
from Products.CSCS.config import PROJECTNAME, EVENT_TYPE
from Products.CSCS.CSCSSchema import schema
from Products.CSCS.interfaces import ICSCSContent
from zope.interface import implements

EventSchema = schema + Schema((
    StringField('event_type',
                index = 'FieldIndex',
                accessor = 'getEventType',
                vocabulary = EVENT_TYPE,
                default = 'Class',
                widget = SelectionWidget(label="Type of the event")
                ),
    StringField('start_date',
                index = 'FieldIndex',
                accessor='getStartDate',
                validators = ('validateStartNEndDate',),
                widget=CalendarWidget(label="Start date of the event")
                ),
    StringField('end_date',
                index = 'FieldIndex',
                accessor='getEndDate',
                widget=CalendarWidget(label="End date of the event")
                ),
    ),)

class CSCSEvent(BaseFolder):
    """An Document type"""
    schema = EventSchema
    archetype_name = portal_type = meta_type = 'CSCSEvent'
    implements(ICSCSContent)

    def tag(self, **kwargs):
        return self.getField('image').tag(self, **kwargs)

registerType(CSCSEvent, PROJECTNAME)
