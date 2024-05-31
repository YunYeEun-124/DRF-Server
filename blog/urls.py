# from django.contrib import admin
# from django.urls import path, include

# from rest_framework.routers import DefaultRouter
# from .views import *

# router = DefaultRouter()
# router.register(r'post', PostViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]
 
from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', PostViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/', PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
]
