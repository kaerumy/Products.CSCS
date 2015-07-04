from Products.Archetypes.public import *
from Products.CSCS.config import PROJECTNAME
from Products.CSCS.CSCSSchema import schema
from Products.CSCS.interfaces import ICSCSContent
from zope.interface import implements

Assignmentschema = schema + Schema((
    FileField('file',
              accessor='getFile',
              widget=FileWidget(label="File Attachment")
              ),
    ),)
                             
class Assignment(BaseFolder):
    """An Document type"""
    schema = Assignmentschema
    archetype_name = portal_type = meta_type = 'Assignment'
    implements(ICSCSContent)

    def tag(self, **kwargs):
        return self.getField('image').tag(self, **kwargs)

registerType(Assignment, PROJECTNAME)

