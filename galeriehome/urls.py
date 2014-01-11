from django.conf.urls import patterns, url

from galeriehome import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^home/', views.index, name='home'),
)
