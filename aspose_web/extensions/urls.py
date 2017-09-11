__author__ = 'waqarali'

from django.conf.urls import url

from . import views

app_name = 'extension'

urlpatterns = [
    url(r'^$', view=views.ExtensionsPrefixes.as_view(), name='index'),
    url(r'^(?P<prefix>[a-z A-Z 0-9]+)/$', view=views.ExtensionsNames.as_view(), name='prefix'),
    url(r'^detail/(?P<pk>[a-z A-Z 0-9 \$ \!]+)/$', view=views.ExtensionDetail.as_view(), name='detail')
]
