from Products.Archetypes.public import *
from Products.CSCS.config import PROJECTNAME
from Products.CSCS.CSCSSchema import schema
from Products.CSCS.interfaces import ICSCSContent
from zope.interface import implements

Bibliographicschema = schema + Schema((
    StringField('title',
                accessor = 'getTitle',
                widget = StringWidget(label='Bibliographic Reference String'),
                ),

    StringField('description',
                accessor = 'getDescription',
                mutator = 'setDescription',
                widget=TextAreaWidget(label='Description',
                description="Insert a brief description of this item here."),
                ),

    StringField('author',
                accessor = 'getAuthor',
                widget = StringWidget(label='Author', description=
                    "Name of author, last name first."),
                ),

    StringField('publication_date',
                accessor = 'getPublicationDate',
                  widget = StringWidget(label="Publication Date"),
                  ),

    StringField('chapter',
                accessor = 'getChapter',
                widget = StringWidget(label='Name of Essay/Chapter'),
                ),

    StringField('publication',
                accessor = 'getPublication',
                widget = StringWidget(label='Publication Title', description=
                    'Name of the book or journal'),
                ),

    StringField('editor',
                accessor = 'getEditor',
                widget = StringWidget(label='Ed(s)', description=
                    'Editors'),
                ),

    StringField('translator',
                accessor = 'getTranslator',
                widget = StringWidget(label='Tr(s)', description=
                    'Translators'),
                ),

    StringField('volume_no',
                accessor = 'getVolumeNo',
                widget = StringWidget(label='Volume No.', description=
                    'The volume number of the publication.'),
                ),

    StringField('publication_place',
                accessor = 'getPublicationPlace',
                widget = StringWidget(label='Place of Publication',
                    description = 'Mandatory for all non-web references.'),
                ),

    StringField('publisher',
                accessor = 'getPublisher',
                widget = StringWidget(label='Publisher', description=
                    'The publisher of the book or journal.'),
                ),

    StringField('page_no',
                accessor = 'getPageNo',
                widget = StringWidget(label='Page Nos.', description=
                    'Page numbers referred to.'),
                ),

    StringField('url',
                accessor = 'getUrl',
                widget = StringWidget(label='URL', description=
                    'The URL for references on the Web.'),
                ),

    DateTimeField('url_date',
                accessor = 'getUrlDate',
                  widget = CalendarWidget(label='URL Date & Time',
                    description = 'The date and time when this URL was viewed.'),
                  ),
    FileField('file',
              accessor='getFile',
              widget=FileWidget(label="File Attachment")
              ),
    ),)

class Bibliographic(BaseFolder):
    """An Document type"""
    schema = Bibliographicschema
    archetype_name = portal_type = meta_type = 'Bibliographic'
    implements(ICSCSContent)

    def tag(self, **kwargs):
        return self.getField('image').tag(self, **kwargs)


registerType(Bibliographic, PROJECTNAME)

