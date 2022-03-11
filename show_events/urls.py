from django.urls import path
from .views import HomeAdmin, HomeUser 


urlpatterns =[ 
    path('admin-home/', HomeAdmin.as_view(), name='admin-home'),
    path('user-home/', HomeUser.as_view(), name='user-home'),
]