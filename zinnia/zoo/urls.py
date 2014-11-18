from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zoo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^comments/', include('django_comments.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
