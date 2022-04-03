from rest_framework import serializers

from measures.models import Measure

class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measure
        fields = ['id', 'name']
