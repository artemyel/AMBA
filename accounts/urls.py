from django.conf.urls import url, include
from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'^', include('registration.backends.hmac.urls')),
    url(r'^(?P<user_id>[0-9]+)/profile/$', views.profile)
]

