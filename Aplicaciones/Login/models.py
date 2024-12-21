from django.db import models

# Create your mode
# DEFINIMOS EL MODELOS PARA EL LOGIN
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=10)  # Guardaremos un hash aquí

    
