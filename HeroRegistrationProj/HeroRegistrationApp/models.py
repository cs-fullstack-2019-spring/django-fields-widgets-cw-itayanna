from django.db import models

# Create your models here.


powerOrMoney = (
    ('rich', 'I am Rich'),
    ('super', 'I have superpowers')
)



lifeChoices = (
    ('Good', 'Good'),
    ('kinda Good', 'Kinda Good'),
    ('Neutral', 'Neutral'),
    ('a little evil', 'A Little Evil'),
    ('Evil', 'Evil')
)


class RegistationModel(models.Model):
    name = models.CharField(max_length=200)
    cityOrigin = models.CharField(max_length=200)
    richOrPowers = models.CharField(max_length=200, choices=powerOrMoney)
    powers = models.CharField(max_length=200)
    integrity = models. CharField(max_length=200, choices=lifeChoices)
    useOfPowers = models.TextField(max_length=600000)
