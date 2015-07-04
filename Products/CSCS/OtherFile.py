from Products.Archetypes.public import *
from Products.CSCS.config import PROJECTNAME
from Products.CSCS.CSCSSchema import schema
from Products.CSCS.interfaces import ICSCSContent
from zope.interface import implements
                             
Otherschema = schema + Schema((
    FileField('file',
              accessor='getFile',
              widget=FileWidget(label="File Attachment")
              ),
    ),)

class OtherFile(BaseFolder):
    """An Document type"""
    schema = Otherschema
    archetype_name = portal_type = meta_type = 'OtherFile'
    implements(ICSCSContent)

    def tag(self, **kwargs):
        return self.getField('image').tag(self, **kwargs)
    
registerType(OtherFile, PROJECTNAME)

