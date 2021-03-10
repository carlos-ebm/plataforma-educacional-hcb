from django.shortcuts import render, get_object_or_404
from shelter.models import Activity
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from registration.models import Profile_activity, Profile
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test

def staff_check(user):
    return user.is_staff

#@user_passes_test(staff_check)

# Create your views here.
#def profile(request):
#    return render(request, "animalProfile/profile.html")

def profile(request, activity_id):
    profile_activity = Profile_activity.objects.all()
    activities = Activity.objects.all()
    activity = get_object_or_404(Activity, activity_id = activity_id)
    return render(request, "animalProfile/profile.html", {'activities':activities, 'profile_activity':profile_activity,'activity':activity})


    

    