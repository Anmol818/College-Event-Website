from django.shortcuts import render
from . models import CollegeEvent
# Create your views here.

def home(request):
    return render(request, 'Events/home.html')

def event(request):
    allEvent = CollegeEvent.objects.all()
    context = {
        "object_list":allEvent,
    }
    return render(request, 'Events/event.html',context)

def contact(request):
    return render(request, 'Events/contact.html')