from django.shortcuts import render
from django.views.generic import TemplateView, ListView


class HomePageView(TemplateView):
    template_name = 'home.html'


class AbotPageView(TemplateView):
    template_name = 'about.html'

