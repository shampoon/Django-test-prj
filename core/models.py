from django.db import models


class Industry(models.Model):
    name = models.CharField('Название индустрии', max_length=255)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField('Название компании', max_length=255)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Human(models.Model):
    name = models.CharField('Имя', max_length=255)
    birth = models.DateField('Дата рождения', null=True, blank=True)
    # age = models.IntegerField('Возраст', null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
