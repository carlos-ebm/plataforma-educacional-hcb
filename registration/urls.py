from django.urls import path
from .views import SignUpView, ProfileUpdate, panel, perfil, login

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('perfil-padrino/', ProfileUpdate.as_view() , name = "perfil-padrino"),
    path('panel/', panel, name="panel"),
    path('perfil/', perfil, name="perfil"),
    path('notificaciones/', perfil, name="notificaciones"),
    path('apadrinamientos/', perfil, name="apadrinamientos"),
]
