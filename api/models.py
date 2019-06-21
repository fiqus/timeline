from django.contrib.gis.db.models import PointField
from django.db import models
from sorl.thumbnail import ImageField


class TimelineEntry(models.Model):
    class Meta:
        verbose_name_plural = "timeline entries"

    datetime = models.DateTimeField()
    title = models.CharField(max_length=512)
    description = models.TextField()
    latlng = PointField(null=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    entry = models.ForeignKey(TimelineEntry, related_name='images', on_delete=models.CASCADE)
    img = ImageField()

    def __str__(self):
        return '%s - %s ' % (self.entry, self.img)
