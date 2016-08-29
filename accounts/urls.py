from django.conf.urls import url, include
from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^add_offer$', views.add_offer, name='add_offer'),
    #url(r'^', include('registration.backends.default.urls')),
    url(r'^(?P<user_id>[0-9]+)/profile/$', views.profile)
]

