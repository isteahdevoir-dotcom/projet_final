# Application de Gestion de Dépenses Personnelles

## Présentation du projet

Cette application web a été développée dans le but de faciliter la gestion des dépenses personnelles. Elle permet aux utilisateurs de suivre, organiser et analyser leurs dépenses quotidiennes à travers une interface simple et intuitive.

Le projet s’inscrit dans une démarche d’apprentissage du framework Django et des concepts fondamentaux du développement web (CRUD, authentification, gestion de base de données).

---

## Objectifs
Permettre aux utilisateurs d’enregistrer leurs dépenses
Offrir une visualisation claire des dépenses effectuées
Organiser les dépenses par catégories
Renforcer les compétences en développement web avec Django

---



## Authentification

Inscription des utilisateurs
Connexion sécurisée
Déconnexion avec redirection

## Gestion des dépenses

Ajout de nouvelles dépenses
Affichage de la liste des dépenses
Association de chaque dépense à un utilisateur

### Catégories

Organisation des dépenses par type :

Logement
Transport
Alimentation
Loisirs
Habillement
Soins de santé

---

## Technologies utilisées

Technologie | Rôle                  

Python      Langage principal     
Django      Framework web         
HTML/CSS    Interface utilisateur 
SQLite      Base de données       


### 2. Créer un environnement virtuel

bash
virtualenv depense_env


### 3. Activer l’environnement virtuel


bash
source depense_env\Scripts\activate


### 4. Installer les dépendances

pip install django


### 5. Appliquer les migrations

python manage.py makemigrations
python manage.py migrate


### 6. Lancer le serveur
python manage.py runserver


### 7. Accéder à l’application

Ouvrir dans le navigateur :

http://127.0.0.1:8000/

## Architecture du projet


depenses_personnelles/

 manage.py
 db.sqlite3
 depenses_personnelles/
 __init__.py
 settings.py
 urls.py
 asgi.py / wsgi.py
 app_depenses/
 models.py
 views.py
 urls.py
 forms.py
 templates/
 migrations/

## Modélisation de la base de données

### 🔹 Modèle Dépense

```python
from django.db import models
from django.contrib.auth.models import User

class Depense(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    titre = models.CharField(max_length=100)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    categorie = models.CharField(max_length=50)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titre


### Explication

ForeignKey : relie chaque dépense à un utilisateur
DecimalField : permet de gérer les montants financiers avec précision
CharField : stocke la catégorie
DateField : enregistre la date de la dépense


## Fonctionnement global

1. L’utilisateur s’inscrit ou se connecte
2. Il accède à son espace personnel
3. Il ajoute une dépense via un formulaire
4. Les données sont enregistrées dans la base SQLite
5. Les dépenses sont affichées sous forme de liste


## Auteure
Projet réalisé par Annaele Pierre

