from django.db import models


class Human(models.Model):
    name = models.CharField('Имя', max_length=255)
    age = models.IntegerField('Возраст', null=True, blank=True)

    def __str__(self):
        return self.name
