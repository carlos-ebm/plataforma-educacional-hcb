from django.shortcuts import render
from .models import Activity

def activities(request):
    allactivities = Activity.objects.all()
    return render(request, "school/activities.html", {"activities": allactivities})


# Create your views here.
