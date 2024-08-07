from django.urls import path
from .views import*

urlpatterns = [
    path('login/',userLogin,name="login"),
    path('browse/',profiles,name="browse"),
    path('register',register,name="register"),
    path('create-profile/',createProfile,name="create-profile"),
    path('logout/',userLogout,name="logout"),
    path('account/',userAccount,name="userAccount"),
    path('delete/',deleteAccount,name="delete"),
]
