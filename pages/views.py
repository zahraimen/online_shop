from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"


class AboutUs(TemplateView):
    template_name = 'pages/aboutus.html'

