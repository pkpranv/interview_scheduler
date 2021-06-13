from rest_framework import serializers

from ..utils import change_time_format

from ..models import Availablity


class UpdateAvailablitySerializer(serializers.Serializer):
    date = serializers.DateField(required=True)
    available_from = serializers.CharField(required=True)
    available_to = serializers.CharField(required=True)

    def create(self, validated_data):
        return Availablity.objects.create(user = self.context.get('user'),
                                   available_from = validated_data['available_from'],
                                   available_to = validated_data['available_to'],
                                   available_date = validated_data['date'])

    def validate(self, data):
        try:
         data['available_from'] = change_time_format(data['available_from'], 1)
         data['available_to'] = change_time_format(data['available_to'], 0)
        except Exception:
            raise serializers.ValidationError({'message' : 'Invalid time format'})
        if data['available_from'] >= data['available_to']:
            raise serializers.ValidationError({'message': 'Avilablity to should be greater than availablity from'})
        return data

    class Meta:
        fields = ( 'date', 'available_from', 'available_to')