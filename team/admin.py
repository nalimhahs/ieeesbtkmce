from django.contrib import admin
import nested_admin

from .models import OfficeBearer, Committee, Team


class OfficeBearerInline(nested_admin.NestedStackedInline):
    model = OfficeBearer
    extra = 1


class CommitteeInline(nested_admin.NestedStackedInline):
    model = Committee
    extra = 1
    inlines = [
        OfficeBearerInline,
    ]


class TeamAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        CommitteeInline,
    ]


admin.site.register(Team, TeamAdmin)
