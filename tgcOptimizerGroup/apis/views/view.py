# import viewsets
from tgcOptimizerGroup.apis.model.entity.models import GeeksModel
from tgcOptimizerGroup.apis.serializers import GeeksSerializer
from rest_framework import viewsets


class GeeksViewSet(viewsets.ModelViewSet):
    queryset = GeeksModel.objects.all()
    serializer_class = GeeksSerializer



