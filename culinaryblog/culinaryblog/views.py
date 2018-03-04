from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView)

class HomePage(TemplateView):
	template_name = "index.html"

class ThanksPage(TemplateView):
	template_name ="thanks.html"

class IntroPage(TemplateView):
	template_name ="intro.html"