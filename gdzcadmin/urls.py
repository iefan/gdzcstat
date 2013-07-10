from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'gdzcadmin.views.home', name='home'),
    # url(r'^gdzcadmin/', include('gdzcadmin.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'gdzc.views.select'),
    url(r'^select/$', 'gdzc.views.select'),
    url(r'^modify/(\d{1,3})/$', 'gdzc.views.modify'),
    url(r'^about/$', 'gdzc.views.about'),

)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )
