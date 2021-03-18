from django.shortcuts import render
from .models import Activity, Activity_profile

def activities(request):
    activities = Activity.objects.all()
    activity_profiles = Activity_profile.objects.all()
    return render(request, "school/activities.html", {"activities": activities, "activity_profiles": activity_profiles})


# Create your views here.
