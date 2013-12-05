from django.conf.urls import patterns, include, url
import website
from website import settings
from website.familiar.views import main, Christmas_list


urlpatterns = patterns('',
    (r'site_media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.STATIC_DOC_ROOT}),
    # url(r'^$', 'website.views.home', name='home'),
    url(r'^$', main, name='main'),
    url(r'^list/', Christmas_list, name='Christmas_list'),
    #url(r'^admin/', include(admin.site.urls)),
)
