from django.contrib import admin
from django.urls import path,include, re_path

    

authapi_urlpatterns = [
   re_path(r'^api/v1/', include('djoser.urls')),
   re_path(r'^api/v1/', include('djoser.urls.authtoken')), 
]