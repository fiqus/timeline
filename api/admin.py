from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib.gis.db.models import PointField
from mapwidgets import GooglePointFieldWidget
from sorl.thumbnail.admin import AdminImageMixin

from api.models import TimelineEntry, Image


class ImageInline(AdminImageMixin, admin.StackedInline):
    model = Image
    extra = 0


@admin.register(TimelineEntry)
class TimelineEntryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        PointField: {"widget": GooglePointFieldWidget}
    }
    list_display = ('datetime', 'title')
    inlines = [ImageInline]
