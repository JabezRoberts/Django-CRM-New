from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead

# Create your views here.

# function based views
def lead_list(request):
    # return HttpResponse("Hello world!")
    # return render(request, 'leads/home_page.html')
    leads = Lead.objects.all() # returns a list of lead objects
    context = {
        "leads": leads
    }
    return render(request, 'leads/lead_list.html', context)
# context is passing information into Django templates


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    
    return render(request, "leads/lead_detail.html", context)