from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register SingerViewSet and SongViewSet with Router
router.register('singer', views.SingerViewSet, basename='singer')
router.register('song', views.SongViewSet, basename='song')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
