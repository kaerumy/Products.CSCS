from Products.Archetypes.public import *
from Products.CSCS.config import PROJECTNAME
from Products.CSCS.CSCSSchema import schema
from Products.CSCS.interfaces import ICSCSContent
from zope.interface import implements
                             
Announcementschema = schema + Schema((
    StringField('announcement_date',
                index = 'FieldIndex',
                accessor='getAnnouncementDate',
                widget=CalendarWidget(label="Announcement date")
                ),
    ),)

class Announcement(BaseFolder):
    """An Document type"""
    schema = Announcementschema
    archetype_name = portal_type = meta_type = 'Announcement'
    implements(ICSCSContent)

    def tag(self, **kwargs):
        return self.getField('image').tag(self, **kwargs)

registerType(Announcement, PROJECTNAME)
