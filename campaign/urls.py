from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.Campaign.as_view()),
    path('count',views.CampaignCount.as_view())
]
