from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    POKEMON_TYPES = {
        ('A', 'Agua'),
        ('F', 'Fuego'),
        ('T', 'Tierra'),
        ('P', 'Planta'),
        ('E', 'Eléctrico'),
        ('L', 'Lagartija')
    }
    type = models.CharField(max_length=30, choices=POKEMON_TYPES, null = False)
    height = models.FloatField(decimal_places=4, max_digits=6)
    weight = models.FloatField(decimal_places=4, max_digits=6)

    def __str__(self):
        return self.name
