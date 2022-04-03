from rest_framework import permissions, viewsets

from measures.models import Measure
from measures.serializers import MeasureSerializer

class MeasureViewSet(viewsets.ModelViewSet):
    queryset = Measure.objects.all()
    serializer_class = MeasureSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
