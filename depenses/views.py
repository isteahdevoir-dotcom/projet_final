from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Depense
from .forms import DepenseForm # type: ignore
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

# 🔹 LISTE DES DÉPENSES
@login_required
def liste_depenses(request):
    depenses = Depense.objects.filter(utilisateur=request.user)
    return render(request, 'depenses/liste.html', {'depenses': depenses})



def register(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        login(request, user)  
        return redirect('liste_depenses')

    return render(request, 'register.html', {'form': form})

@login_required
def detail_depense(request, id):
    depense = get_object_or_404(
        Depense,
        id=id,
        utilisateur=request.user  
    )
    return render(request, 'depenses/detail.html', {'depense': depense})


# 🔹 AJOUTER UNE DÉPENSE
@login_required
def ajouter_depense(request):
    form = DepenseForm(request.POST or None)

    if form.is_valid():
        depense = form.save(commit=False)
        depense.utilisateur = request.user  
        depense.save()
        return redirect('liste_depenses')

    return render(request, 'depenses/form.html', {'form': form})


# 🔹 MODIFIER UNE DÉPENSE
@login_required
def modifier_depense(request, id):
    depense = get_object_or_404(
        Depense,
        id=id,
        utilisateur=request.user  
    )

    form = DepenseForm(request.POST or None, instance=depense)

    if form.is_valid():
        form.save()
        return redirect('liste_depenses')

    return render(request, 'depenses/form.html', {'form': form})


# SUPPRIMER UNE DÉPENSE

@login_required
def supprimer_depense(request, id):
    depense = get_object_or_404(
        Depense,
        id=id,
        utilisateur=request.user  # 🔐 sécurité
    )

    if request.method == 'POST':
        depense.delete()
        return redirect('liste_depenses')

    return render(request, 'depenses/confirm_delete.html', {
        'depense': depense
    })