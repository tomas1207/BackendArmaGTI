from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.UserCreator.as_view()),
    path('email-verify/', views.VerifyEmail.as_view(),name='emailVerify'),
    path('logout/', views.Logout.as_view())
]
