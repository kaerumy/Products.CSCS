from Products.CMFCore.utils import getToolByName
from Products.contentmigration.archetypes import ATFolderMigrator
from Products.contentmigration.walker import CustomQueryWalker
from zope.component.hooks import getSite
from logging import getLogger
logger = getLogger('Products.CSCS Upgrade')
from StringIO import StringIO
from collective.contentleadimage.leadimageprefs import ILeadImagePrefsForm


def upgrade(context, logger=None):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-Products.CSCS.upgrade:to3')
    site = getSite()
    migrate_foldertypes(site)    

class FolderMigrator(object, ATFolderMigrator):

    walker = CustomQueryWalker
    src_meta_type = ''
    src_portal_type = ''
    dst_meta_type = 'ATFolder'
    dst_portal_type = 'Folder'

    def __init__(self, *args, **kwargs):
        self.old = args[0] #The original object
        self.orig_id = self.old.id #The original object id
        self.old_id = 'old_%s' % self.orig_id #Change the old id to this after copying
        self.new_id = self.old.id #Make the new object id this
        self.parent = self.old.getParentNode() #Grap the object's parent
        ATFolderMigrator.__init__(self, *args, **kwargs)


    def custom(self):
        # set default allowed types
        fti = self.old.portal_types.get(self.old.getPortalTypeName())
        allowed_types = fti.allowed_content_types
        folder = self.new
        old = self.old

        folder.setLocallyAllowedTypes(allowed_types)
        folder.invokeFactory(type_name="CSCSContent", id='default_content')

        item = folder['default_content']

        fields_map = {'image':'leadImage',
                      'short_description': 'description'}
        for fn in old.Schema().keys():
            if fn in ['id', 'creation_date', 'modification_date']:
                continue
            field = old.Schema()[fn]
            value = field.get(old)
            newfn = fields_map.get(fn, fn)
            item.Schema()[newfn].set(item, value)

        workflowTool = getToolByName(item, "portal_workflow")
        workflowTool.doActionFor(item, 'submit')
        workflowTool.doActionFor(item, 'publish')
        default_view = fti.defaultView(old)
        item.setLayout(default_view)
        item.reindexObject()
        folder.setDefaultPage('default_content')


class CSCSObjectMigrator(ATFolderMigrator):
    walker = CustomQueryWalker
    src_meta_type = 'CSCSObject'
    src_portal_type = 'CSCSObject'
    dst_meta_type = 'CSCSContent'
    dst_portal_type = 'CSCSContent'
    fields_map = {'short_description': 'description',
                  'image': 'leadImage'}


def set_linkintegrity(val):
    site = getSite()
    site_prop = site.portal_properties.site_properties
    site_prop.enable_link_integrity_checks = val
    

def migrate_foldertypes(site):

    cli_prefs = ILeadImagePrefsForm(site)

    allowed_cli = list(cli_prefs.allowed_types)
    allowed_cli.append('CSCSContent')
    cli_prefs.allowed_types = allowed_cli

    foldertypes = ['Announcements', 'AnnouncementsFolder', 
                    'AudioFiles', 'CoursesFolder', 'Courses',
                    'CSCSEventsFolder', 'CSCSEvents', 
                    'DataArchive', 'DataBoxs', 'FAQs',
                    'Fellowships', 'IRPs', 'LibraryServices',
                    'MediaServices', 'Modules', 'MovingImages',
                    'OtherFiles', 'Papers', 'Photos', 
                    'PublicationsFolder', 'Publications',
                    'TextFiles']

    set_linkintegrity(False)
    migrators = [CSCSObjectMigrator]
    for t in foldertypes:
        m = type('%sMigrator' % t, (FolderMigrator,), {})
        m.src_meta_type = t
        m.src_portal_type = t
        migrators.append(m)

    #Run the migrations
    for migrator in migrators:
        logger.info("-- Migrating %ss --\n\n" % migrator.src_meta_type)
        walker = migrator.walker(site, migrator)
        walker.go()
        logger.info(walker.getOutput())

    site.portal_types.manage_delObjects(foldertypes)
    set_linkintegrity(True)
