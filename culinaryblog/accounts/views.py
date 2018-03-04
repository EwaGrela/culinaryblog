from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from . import forms
# from accounts.forms import UserCreateForm
from django.views.generic import CreateView


# Create your views here.
class SignUpView(CreateView):
	form_class = forms.UserCreateForm
	success_url = reverse_lazy('login')
	template_name = "accounts/signup.html"

	



