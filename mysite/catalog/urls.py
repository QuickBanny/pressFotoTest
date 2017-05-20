from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from mysite import settings
from catalog.views import home 
from catalog.views import about
from catalog.views import show_image
from catalog.views import search_form
from catalog.views import search

urlpatterns = [
    url(r'^$', home, name='home',),
    url(r'^about/$', about, name='about'),
    url(r'^images/(?P<image_id>[0-9]+)/$', show_image, name='image'),
    url(r'^search-form/$', search_form, name='search_form'),
    url(r'^search/$', search, name='search')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()