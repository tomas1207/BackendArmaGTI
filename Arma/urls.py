from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.MissionStatus.as_view()),
    path('medic', views.MedicStatus.as_view()),
]
