from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.missionsStatus.as_view()),
    # path('count', views.missionsCount.as_view()),
]