from Products.Archetypes.public import listTypes, process_types
from Products.CMFCore import utils
from Products.CMFCore.DirectoryView import registerDirectory
from config import *

from Products.validation import service
from Products.CSCS.validators import ValidateStartNEndDate

validation = service.Service()
validation.register(ValidateStartNEndDate("validateStartNEndDate"))

registerDirectory(SKINS_DIR, GLOBALS)

def initialize(context):
    """Initialize Product."""
    import Announcement, Announcements, AnnouncementsFolder, Assignment, People, \
           AudioFile, AudioFiles, CSCSEvent, CSCSEvents, CSCSEventsFolder, \
           CSCSObject, Courses, CoursesFolder, DataArchive, DataBox, DataBoxs, \
           FAQ, FAQs, Fellowship, Fellowships, IRP, IRPs, Bibliographic, \
           LibraryService, LibraryServices, MediaService, MediaServices, \
           Modules, MovingImage, MovingImages, OtherFile, OtherFiles, Papers, Photo, \
           Photos, Publication, Publications, PublicationsFolder, TextFile, TextFiles, \
           CSCSPeople, CSCSContent

    content_types, constructors, ftis = process_types(listTypes(PROJECTNAME),
                                                      PROJECTNAME)
    utils.ContentInit(PROJECTNAME + 'Content',
                      content_types = content_types,
                      permission = "Add CSCSItem",
                      extra_constructors = constructors,
                      fti = ftis,
                      ).initialize(context)
