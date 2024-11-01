from tgcOptimizerGroup.apis.services.hello import getHello
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def get_geeks(request):
    name = request.GET.get('name', 'fajri')
    data = getHello(name)
    return Response(data,status=status.HTTP_200_OK)
