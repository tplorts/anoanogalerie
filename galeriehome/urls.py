from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView

from galeriehome import views


blog_redirect = RedirectView.as_view(url='http://anoanogalerie.blogspot.jp/')

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^concept/', views.concept, name='concept'),
    url(r'^schedule/', views.schedule, name='schedule'),
    url(r'^news/', blog_redirect, name='news'),
    url(r'^guide/', views.guide, name='guide'),
    url(r'^access/', views.access, name='access'),
)
