from django.conf.urls import include, url
from django.contrib import admin
from web_app import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'Web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/',views.index),
]
