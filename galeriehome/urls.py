from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView

from galeriehome import views


blog_redirect = RedirectView.as_view(url='http://anoanogalerie.blogspot.jp/')
pdf_redirect = RedirectView.as_view(url='http://s3-ap-northeast-1.amazonaws.com/anoanogalerie-static/static/media/documents/ano-ano-gallerie-floor-guide.pdf')


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^concept/', views.concept, name='concept'),
    url(r'^schedule/$', views.schedule, name='schedule'),
    url(r'^schedule/past/$', views.schedule_past, name='schedule past'),
    url(r'^webshop/$', views.webshops, name='webshops'),
    url(r'^webshop/(?P<shopKey>\d+)/$', views.webshop, name='webshop'),
    url(r'^news/', blog_redirect, name='news'),
    url(r'^guide/$', views.guide, name='guide'),
    url(r'^guide/pdf/$', pdf_redirect, name='Guide PDF'),
    url(r'^access/', views.access, name='access'),
)
