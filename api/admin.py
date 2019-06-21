from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from sorl.thumbnail.admin import AdminImageMixin

from api.models import TimelineEntry, Image


class ImageInline(AdminImageMixin, admin.StackedInline):
    model = Image
    extra = 0


@admin.register(TimelineEntry)
class TimelineEntryAdmin(OSMGeoAdmin):
    list_display = ('datetime', 'title')
    inlines = [ImageInline]
