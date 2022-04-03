from django.contrib import admin

from .models import Track, Album, Artist

# Register disks models
admin.site.register(Track)
admin.site.register(Album)
admin.site.register(Artist)
