# basic URL Configurations
from tgcOptimizerGroup.apis.views.view import GeeksViewSet
from tgcOptimizerGroup.apis.controller import GeeksController
from django.urls import include, path
from rest_framework import routers

# define the router
router = routers.DefaultRouter()

# # define the router path and viewset to be used
router.register(r'api/geeks', GeeksViewSet)

# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
    path('api/hello', GeeksController.get_geeks)
]