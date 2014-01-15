from django.conf.urls import patterns, url

from galeriehome import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^concept/', views.concept, name='concept'),
    url(r'^schedule/', views.schedule, name='schedule'),
    url(r'^news/', views.news, name='news'),
    url(r'^guide/', views.guide, name='guide'),
    url(r'^access/', views.access, name='access'),

    url(r'^sandbox/', views.sandbox, name='sandbox'),
)
