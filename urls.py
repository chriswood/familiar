from django.conf.urls import patterns, include, url
import website
from website import settings


urlpatterns = patterns('',
    (r'site_media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.STATIC_DOC_ROOT}),
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'website.familiar.views.main', name='main')
    #url(r'^admin/', include(admin.site.urls)),
)
