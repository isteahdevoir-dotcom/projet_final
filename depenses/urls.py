from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_depenses, name='liste_depenses'),
    path('ajouter/', views.ajouter_depense, name='ajouter_depense'),
    path('modifier/<int:id>/', views.modifier_depense, name='modifier_depense'),
    path('supprimer/<int:id>/', views.supprimer_depense, name='supprimer_depense'),
    path('register/', views.register, name='register'),
    path('detail/<int:id>/', views.detail_depense, name='detail_depense'),
    
]