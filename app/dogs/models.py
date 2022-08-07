from django.db import models


class AvaliableDogs(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    age = models.CharField(max_length=5)
    breed = models.CharField(max_length=50)
    temperament = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name
