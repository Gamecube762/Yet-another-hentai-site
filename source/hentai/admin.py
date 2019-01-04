from django.contrib import admin
from hentai.models import *

# Register your models here.

admin.site.register(Language)
admin.site.register(Series)
admin.site.register(Description)
admin.site.register(Video)
admin.site.register(VideoTag)
admin.site.register(TagLan)

# The code loads all of the models to the admin site
# It really helps with the testing