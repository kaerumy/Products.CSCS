from zope.component import adapts
from zope.interface import implements
from archetypes.schemaextender.interfaces import ISchemaExtender
from Products.ATContentTypes.interface import IATDocument
from Products.Archetypes.atapi import StringField
from archetypes.schemaextender.field import ExtensionField
from Products.Archetypes.atapi import StringWidget

class ExtendedStringField(ExtensionField, StringField): pass

class RemoteUrlExtender(object):
    adapts(IATDocument)
    implements(ISchemaExtender)

    fields = [
        ExtendedStringField('remoteUrl',
            required=False,
            searchable=True,
            # either mailto, absolute url or relative url
            validators = (),
            widget = StringWidget(
                description = '',
                label = u'URL',
                maxlength = '511',
            )),
    ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields



from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

class RemoteUrlViewlet(ViewletBase):
    render = ViewPageTemplateFile('remote_url.pt')

