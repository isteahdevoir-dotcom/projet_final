from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Depense(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    titre = models.CharField(max_length=100)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    categorie = models.CharField(max_length=50)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titre