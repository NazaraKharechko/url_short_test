from django.conf.urls import url
from django.urls import path
from . import views
from .views import LinkCreate, LinkShow, RedirectToLongURL

urlpatterns = [
    # path('', views.mam),
    path('', LinkCreate.as_view(), name='home'),
    path('link/<int:pk>', LinkShow.as_view(), name='link_show'),
    path(r'r/<short_url>', RedirectToLongURL.as_view(), name='redirect_short_url'),
]
