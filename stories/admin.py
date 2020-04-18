from django.contrib import admin
import nested_admin

from .models import  Story, StoryImage

class StoryImageInline(nested_admin.NestedTabularInline):
    model = StoryImage

class StoryAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        StoryImageInline,
    ]

admin.site.register(Story, StoryAdmin)
