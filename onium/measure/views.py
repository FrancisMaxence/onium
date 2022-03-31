from rest_framework import permissions, viewsets

from onium.measure.models import Measure
from onium.measure.serializers import MeasureSerializer

class MeasureViewSet(viewsets.ModelViewSet):
    queryset = Measure.objects.all()
    serializer_class = MeasureSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
