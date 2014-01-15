from django.conf.urls import patterns, url

from galeriehome import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^idea/', views.idea),
    url(r'^schedule/', views.schedule),
    url(r'^news/', views.news),
    url(r'^guide/', views.guide),
    url(r'^access/', views.access),

    url(r'^sandbox/', views.sandbox, name='sandbox'),
)
