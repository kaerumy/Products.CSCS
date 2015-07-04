from Products.Archetypes.public import *
from Products.CSCS.config import PROJECTNAME
from Products.CSCS.CSCSSchema import schema
from Products.CSCS.interfaces import ICSCSContent
from zope.interface import implements
                             
Photoschema = schema + Schema((
    FileField('file',
              accessor='getFile',
              widget=FileWidget(label="File Attachment")
              ),
    ),)

class Photo(BaseFolder):
    """An Document type"""
    schema = Photoschema
    archetype_name = portal_type = meta_type = 'Photo'
    implements(ICSCSContent)

    def tag(self, **kwargs):
        return self.getField('image').tag(self, **kwargs)
    

registerType(Photo, PROJECTNAME)

