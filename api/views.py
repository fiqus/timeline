from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from sorl.thumbnail import get_thumbnail

from api.models import TimelineEntry, Image


class ImageSerializer(ModelSerializer):
    thumbnail = SerializerMethodField()

    class Meta:
        model = Image
        fields = ("img", "thumbnail")

    def get_thumbnail(self, obj):
        thumb = get_thumbnail(obj.img, "100x100")
        return {
            "src": thumb.url,
            "width": thumb.width,
            "height": thumb.height
        }


class TimelineEntrySerializer(ModelSerializer):
    lat_lng = SerializerMethodField()
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = TimelineEntry
        fields = '__all__'

    def get_lat_lng(self, obj):
        return reversed(obj.latlng.coords)


class TimelineEntryView(ReadOnlyModelViewSet):
    queryset = TimelineEntry.objects.all().order_by('datetime')
    serializer_class = TimelineEntrySerializer
