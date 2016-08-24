from django.conf.urls import url
from . import views

app_name = 'main'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<category_name>[-\w]+)/$', views.CategoryView.as_view()),
    url(r'^offer/(?P<offer_id>[0-9]+)/$', views.offer_view, name='offer'),

]


