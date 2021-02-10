from django.conf.urls import url
from django.urls import path
from . import views
from .views import LinkCreate, LinkShow, RedirectToLongURL

urlpatterns = [
    # path('', views.mam),
    path('', LinkCreate.as_view(), name='home'),
    path(r'link/(?P<pk>\d+)', LinkShow.as_view(), name='link_show'),
    path(r'r/(?P<short_url>\w+)', RedirectToLongURL.as_view(), name='redirect_short_url'),
]
