from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.login,name='signup'),
    path('userpage/',views.userpage,name='userpage'),
    path('logout/',views.logout,name='logout')
]
