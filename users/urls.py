from django.urls import path,include
from . import views
urlpatterns = [
    path('register/', views.UserCreator.as_view()),
    path('login/', views.login.as_view()),
    path('email-verify/', views.VerifyEmail.as_view(),name='emailVerify'),
    path('logout/', views.Logout.as_view())
]
