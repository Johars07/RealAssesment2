from django import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Newsstuff


# Create your views here.

def index(request):
    latest_articles = Newsstuff.objects.order_by('-pub_date')

    template = loader.get_template('news/index.html')
    context = {
        'latest_articles': latest_articles,
    }

    return HttpResponse(template.render(request))
