fron django.db import models

class Stagiaire(doles.Model):
    nom = models.CharField(max_length = 60)
    prenom = models.CharField(max_length = 60)
