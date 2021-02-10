from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from shortener.views import RedirectView
from django.conf import settings
from .models import Link, Statistics_Data
from django.shortcuts import redirect

from django.http import HttpRequest
from django.template import *
import datetime
from requests import request


def get_stat():
    t = Template("{{ request.META.HTTP_REFERER }}")
    req = HttpRequest()
    req.META['HTTP_REFERER'] = settings.SITE_URL
    c = Context({'request': req})
    referer = t.render(c)

    time = datetime.datetime.now()

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(f'Тутт реф {referer} та час {time} і IP {ip}')
    purchase = Statistics_Data(referer=referer, time=time, ip=ip)
    return purchase.save()


def mam(request):
    return render(request, 'url/base.html')


# Create your views here.
class LinkCreate(CreateView):
    model = Link
    fields = ["url"]

    def form_valid(self, form):
        prev = Link.objects.filter(url=form.instance.url)
        if prev:
            return redirect("link_show", pk=prev[0].pk)
        return super(LinkCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(LinkCreate, self).get_context_data(**kwargs)
        # Passing link_list to display original and short_url in link_form.html
        context['link_list'] = Link.objects.all().order_by('-id')[:10]
        # Passing site_url to display domain base
        context['site_url'] = settings.SITE_URL
        get_stat()
        return context


class LinkShow(DetailView):
    model = Link

    def get_context_data(self, **kwargs):
        context = super(LinkShow, self).get_context_data(**kwargs)
        context['site_url'] = settings.SITE_URL
        get_stat()
        return context


class RedirectToLongURL(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        short_url = kwargs['short_url']
        get_stat()
        return Link.expand(short_url)
