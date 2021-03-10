from django.shortcuts import render
from .models import Activity

def sponsoring(request):
    activities = Activity.objects.all()
    return render(request, "shelter/sponsoring.html", {"activities": activities})


# Create your views here.
