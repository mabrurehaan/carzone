from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.photo.url))

    thumbnail.short_description = 'Photo'

    list_display = ('id', 'thumbnail', 'full_Name', 'designation', 'created_Date')
    list_display_links = ('id', 'thumbnail', 'full_Name',)
    search_fields = ('full_Name', 'Wing_Name', 'designation')
    list_filter = ('designation',)

admin.site.register(Team, TeamAdmin)