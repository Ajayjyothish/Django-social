from django.shortcuts import render
from django.http import HttpResponse
from .models import Page, Section
from django.views.generic import TemplateView

# Create your views here.
def home_view(request):
    
    my_context = {
        'my_name' : 'Ajay',
        'my_number' : 12324
    
    }

    return render(request,"hello.html",my_context)

class contact_view(TemplateView):
    template_name = "contact.html"