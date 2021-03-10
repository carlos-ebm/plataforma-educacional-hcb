from django.urls import path
from . import views


urlpatterns =[
    path('perfil-animal/<int:animal_id>/', views.profile , name = "perfil-animal"),
    #path('perfil-padrino/<int:id>/', sponsorProfile_views.profile , name = "perfil-padrino"),
    #path('perfil-animal/', views.profile , name = "perfil-animal"),

]