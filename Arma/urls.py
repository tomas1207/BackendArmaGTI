from django.urls import path,include
from . import views
urlpatterns = [
    path('medic', views.MedicStatus.as_view()),
    path('unconscious',views.unconsciousStatus.as_view()),
    path('shootsfired',views.shootsFiredStatus.as_view()),
]
