from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView
from django.core.urlresolvers import reverse_lazy
from .models import *


# Create your views here.

class Home(TemplateView):
  template_name = "home.html"

class ContactCreateView(CreateView):
  model = Contact
  template_name = "contact/contact_form.html"
  fields = ['Name', 'Message','EMail',]
  success_url = reverse_lazy('success')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(ContactCreateView, self).form_valid(form)

class Success(TemplateView):
  template_name = "success.html"

class ContactDetailView(DetailView):
  model = Contact
  template_name = 'contact/contact_detail.html'

