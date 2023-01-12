"""logistic_track URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from track_truck import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.trip_view,name='main'),
    path('trip_track_view',views.trip_track_view,name='trip_track_view'),
    path('track_details',views.track_details,name='track_details'),
    path('track_details_2',views.track_details_2,name='track_details_2')


]
