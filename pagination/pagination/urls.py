from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.StudentList.as_view()),
]
