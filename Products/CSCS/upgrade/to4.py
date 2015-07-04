from zope.component.hooks import getSite
from Products.CSCS.interfaces import ICSCSContent

def upgrade(context, logger=None):
    site = getSite()
    for i in site.portal_catalog(
        object_provides=ICSCSContent.__identifier__
        ):
        obj = i.getObject()
        obj.setDescription(obj.short_description)
        print 'fixing %s' % obj.absolute_url()
