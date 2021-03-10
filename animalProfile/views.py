from django.shortcuts import render, get_object_or_404
from shelter.models import Animal, Sponsor, Animal_sponsor
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from registration.models import Profile_animal, Profile
from .forms import Profile_animalForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test

def staff_check(user):
    return user.is_staff

#@user_passes_test(staff_check)

# Create your views here.
#def profile(request):
#    return render(request, "animalProfile/profile.html")

def profile(request, animal_id):
    sponsor = Sponsor.objects.all()
    animal_sponsor = Animal_sponsor.objects.all()
    profile_animal = Profile_animal.objects.all()
    animals = Animal.objects.all()
    animal = get_object_or_404(Animal, animal_id = animal_id)
    return render(request, "animalProfile/profile.html", {'animals':animals, 'animal':animal, 'sponsors':sponsor, 'animal_sponsors':animal_sponsor, 'profile_animals':profile_animal})

def validation(request, animal_id, sponsor_id):
    animal = get_object_or_404(Animal, animal_id = animal_id)
    sponsor = get_object_or_404(Sponsor, sponsor_id = sponsor_id)
    return render(request, "animalProfile/validation.html", {'animal':animal, 'sponsor':sponsor})

class Profile_animalCreate(CreateView):
    form_class = Profile_animalForm
    template_name = 'animalProfile/validation.html'
    #anima2 = get_object_or_404(Animal, animal_id = kwargs['animal_id'])

    def form_valid(self, form):
        animal_id = self.kwargs['animal_id']
        #sponsor_id = self.kwargs['sponsor_id']
        profile_id = self.request.user.id
        form.instance.animal = get_object_or_404(Animal, animal_id = animal_id)
        form.instance.sponsor = self.kwargs['sponsor_id']
        form.instance.profile = get_object_or_404(Profile, user_id = profile_id)
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('inicio') + '?ok'
    

    