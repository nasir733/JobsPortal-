from django.urls import path
from .views import  login, register, logout, complete_verification
urlpatterns = [
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('logout', logout, name='logout'),
    path(
        "verify/<str:key>/", complete_verification, name="complete-verification"
    ),


]
