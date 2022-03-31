from rest_framework import serializers

from onium.measure.models import Measure

class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measure
        fields = ['id', 'name']
