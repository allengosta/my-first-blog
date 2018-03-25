from django.contrib.auth.views import login, logout
from django.conf.urls import include, url


urlpatterns = [
    # существующие шаблоны располагаются здесь...
    url(r'^accounts/login/$',  login),
    url(r'^accounts/logout/$', logout),
]