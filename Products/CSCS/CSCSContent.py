from Products.Archetypes.public import *
from Products.ATContentTypes.content.base import ATCTContent, registerATCT
from Products.ATContentTypes.interfaces import IATContentType
from Products.ATContentTypes.content.schemata import ATContentTypeSchema
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from Products.CSCS.config import PROJECTNAME
from Products.CSCS.CSCSSchema import schema
from collective.contentleadimage.interfaces import ILeadImageable
from zope.interface import implements
from Products.CSCS.interfaces import ICSCSContent
from wcc.carousel.interfaces import ICarouselImageEnabled

CSCSContentSchema = ATContentTypeSchema.copy() + Schema((
    schema['full_description'],
    schema['url'],
))

CSCSContentSchema['description'].widget = TextAreaWidget(
    label="Short description",
    maxlength="255",
    rows=3
)

finalizeATCTSchema(CSCSContentSchema)

#CSCSContentSchema.changeSchemataForField('description', 'default')
#CSCSContentSchema.moveField('description', after='title')

class CSCSContent(ATCTContent):
    """An Document type"""
    schema = CSCSContentSchema
    archetype_name = portal_type = meta_type = 'CSCSContent'
    implements(ICSCSContent, ILeadImageable, ICarouselImageEnabled)

    @property
    def short_description(self):
        return self.getShortDescription()

    def getShortDescription(self):
        return self.Description()

    def getImage(self):
        return self.getField('leadImage').get(self)

    def tag(self, **kwargs):
	field = self.getField('image')
        if field is None:
            return ""
        return self.getField('image').tag(self, **kwargs)



registerATCT(CSCSContent, PROJECTNAME)
