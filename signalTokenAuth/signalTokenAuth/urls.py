from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register StudnetViewSet With Router
router.register('studentapi', views.StudentModelViewSet, basename = 'Student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/',include('rest_framework.urls', namespace='rest_framework')),
]