from django.urls import path
from .views import SignUpView, ProfileUpdate, perfil, login

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('perfil-usuario/', ProfileUpdate.as_view() , name = "perfil-usuario"),
    path('perfil/', perfil, name="perfil"),
]
