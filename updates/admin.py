from django.contrib import admin
import nested_admin

from .models import  Update, UpdateImage, Contact

class UpdateContactInline(nested_admin.NestedTabularInline):
    model = Contact
    extra = 1

class UpdateImageInline(nested_admin.NestedTabularInline):
    model = UpdateImage
    extra = 1

class UpdateAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        UpdateImageInline,
        UpdateContactInline,
    ]

admin.site.register(Update, UpdateAdmin)
