from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead

# Create your views here.

# function based views
def home_page(request):
    # return HttpResponse("Hello world!")
    # return render(request, 'leads/home_page.html')
    leads = Lead.objects.all() # returns a list of lead objects
    context = {
        "leads": leads
    }
    return render(request, 'second_page.html', context)
# context is passing information into Django templates

