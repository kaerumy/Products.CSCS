from Products.Archetypes.public import *
from Products.CSCS.config import PROJECTNAME
from Products.CSCS.CSCSSchema import schema
from Products.CSCS.interfaces import ICSCSContent
from zope.interface import implements
from wcc.carousel.interfaces import ICarouselImageEnabled
                             
class IRP(BaseFolder):
    """An Document type"""
    schema = schema
    archetype_name = portal_type = meta_type = 'IRP'
    implements(ICSCSContent, ICarouselImageEnabled)

    def tag(self, **kwargs):
        return self.getField('image').tag(self, **kwargs)


    
registerType(IRP, PROJECTNAME)

