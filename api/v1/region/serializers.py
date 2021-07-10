from rest_framework import serializers

from region.models import Region


class RegionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('text',)

    def to_representation(self, instance: Region):
        data = super(RegionsSerializer, self).to_representation(instance)
        data['value'] = instance.get_value
        return data
