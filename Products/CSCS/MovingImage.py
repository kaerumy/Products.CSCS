from Products.Archetypes.public import *
from Products.CSCS.config import PROJECTNAME
from Products.CSCS.CSCSSchema import schema
from Products.CSCS.interfaces import ICSCSContent
from zope.interface import implements

                             
MovingImageschema = schema + Schema((
    FileField('file',
              accessor='getFile',
              widget=FileWidget(label="File Attachment")
              ),
    ),)

class MovingImage(BaseFolder):
    """An Document type"""
    schema = MovingImageschema
    archetype_name = portal_type = meta_type = 'MovingImage'

    def tag(self, **kwargs):
        return self.getField('image').tag(self, **kwargs)

registerType(MovingImage, PROJECTNAME)

