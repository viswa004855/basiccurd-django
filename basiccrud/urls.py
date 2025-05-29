from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crud/',include('crud.urls')), #make sure points to your app's URLS
]
