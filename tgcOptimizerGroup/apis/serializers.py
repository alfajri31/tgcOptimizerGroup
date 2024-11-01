# import serializer from rest_framework
from tgcOptimizerGroup.apis.model.entity.models import GeeksModel
from rest_framework import serializers

# Create a model serializer
class GeeksSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = GeeksModel
        fields = ('title', 'description')