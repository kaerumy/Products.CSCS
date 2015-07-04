from Products.Archetypes.public import *
from Products.CSCS.config import PROJECTNAME

schema = BaseFolderSchema.copy() + Schema((
    StringField('id',
                accessor='getId',
                widget=IdWidget(visible={'edit':'invisible'}),
                ),
    StringField('title',
                required=1,
                searchable=1,
                accessor='Title',
                widget=StringWidget(label_msgid="label_title",),
                ),
    TextField('short_description',
              index = 'FieldIndex',
              accessor='getShortDescription',
              widget=TextAreaWidget(label="Short description",
                                    maxlength="255",
                                    rows=3)),
    TextField('full_description',
              accessor='getFullDescription',
              allowable_content_types = ('text/plain',
                                         'text/structured',
                                         'text/html',
                                         'application/msword',
                                         'application/pdf',
                                         ),
              default_output_type='text/html',
              widget=RichWidget(label='Full description',
                                rows=6)),
    ),)

class CSCSPeople(BaseFolder):
    """An Document type"""
    schema = schema
    archetype_name = portal_type = meta_type = 'CSCSPeople'
    
registerType(CSCSPeople, PROJECTNAME)


