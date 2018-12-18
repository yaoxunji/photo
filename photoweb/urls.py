from django.conf.urls import include, url
from django.contrib import admin
from photo import views as pv
urlpatterns = [
    # Examples:
    # url(r'^$', 'photoweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', pv.time),
    url(r'^/', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
