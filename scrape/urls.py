from django.urls import path

from . import views

app_name = 'scrape'
urlpatterns = [
    path('', views.ScrapeView.as_view(), name='scrape'),
    path('land', views.waittime_land, name='land'),
    path('sea', views.waittime_sea, name='sea'),
]