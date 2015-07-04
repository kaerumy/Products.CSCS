from Products.Archetypes.public import *
from Products.CSCS.config import PROJECTNAME
from Products.CSCS.CSCSSchema import schema
from Products.CSCS.interfaces import ICSCSContent
from zope.interface import implements

Audioschema = schema + Schema((
    FileField('file',
              accessor='getFile',
              widget=FileWidget(label="File Attachment")
              ),
    ),)
                             
class AudioFile(BaseFolder):
    """An Document type"""
    schema = Audioschema
    archetype_name = portal_type = meta_type = 'AudioFile'
    implements(ICSCSContent)

    def tag(self, **kwargs):
        return self.getField('image').tag(self, **kwargs)

registerType(AudioFile, PROJECTNAME)

