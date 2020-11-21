from django.contrib import admin
from django.urls import path, include

from . import views

app_name = "api"

urlpatterns = [
    path('category/', views.PetCategory.as_view()), # get
    path('pet/', views.PetCard.as_view()), # post (id)
    path('hb/', views.HappyPet.as_view()), # get
    path('popular/', views.Popular.as_view()),
]