from django.conf.urls import url
from search import views

urlpatterns = [
    url(r'^searchword/$', views.SearchListAPIView, name='search'),
    url(r'^home/$', views.Home, name= 'home'),
]