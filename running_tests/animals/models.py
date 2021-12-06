from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=200)
    sound = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def speak(self):
        return f'The {self.name} says {self.sound}'
