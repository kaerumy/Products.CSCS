from Products.Archetypes.public import *

schema = BaseFolderSchema.copy() + Schema((
    StringField('id',
                accessor='getId',
                searchable=1,
                widget=IdWidget(visible={'edit':'invisible'}),
                ),
    StringField('title',
                required=1,
                searchable=1,
                accessor='Title',
                widget=StringWidget(label_msgid="label_title",),
                ),
    TextField('full_description',
              accessor='getFullDescription',
              searchable=1,
              allowable_content_types = ('text/plain',
                                         'text/structured',
                                         'text/html',
                                         'application/msword',
                                         'application/pdf',
                                         ),
              default_output_type='text/html',
              widget=RichWidget(label='Full description',
                                rows=6)),
    StringField('url',
                accessor='getURL',
                widget=StringWidget(label="URL"),
                ),
    ImageField('image',
               accessor='getImage',
               original_size=(600,600),
               widget=ImageWidget(label="Image")
               ),
    ),)

schema['description'].widget = TextAreaWidget(
    label="Short description",
    maxlength="255",
    rows=3
)
