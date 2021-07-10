from rest_framework import serializers

from region.models import Region


class RegionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('text',)