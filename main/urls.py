from django.conf.urls import url
from . import views


app_name = 'main'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^(?P<category_name>[-\w]+)/$', views.category_view)
]

