from django.db import models
from datetime import datetime

class City(models.Model):
    city_name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.city_name


class Haven(models.Model):
    haven_name = models.TextField(default='', unique=True)
    
    def __str__(self):
        return self.haven_name


class Gender(models.Model):
    gender = models.CharField(max_length=50, unique=True, default='')

    def __str__(self):
        return self.gender


class PetsType(models.Model):
    pets_type = models.CharField(max_length=50, unique=True, default='')
    
    def __str__(self):
        return self.pets_type

class Pets(models.Model):
    name = models.CharField(max_length=100)
    profile_link = models.TextField(default='')
    haven = models.ForeignKey(Haven, on_delete=models.CASCADE, related_name='pets_haven')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='pets_city')
    race = models.CharField(max_length=100)
    type_of_pet = models.ForeignKey(PetsType, on_delete=models.CASCADE, related_name='pet_type')
    date_of_birth = models.DateField(default='01.01.0000')
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name='pet_gender')
    in_favorites = models.IntegerField(default=0)
    found_home = models.BooleanField(default=False)
    take_to_home = models.IntegerField(default=0)
    take_to_walk = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Transactions(models.Model):
    pet_name = models.CharField(max_length=100)
    pet_id = models.IntegerField(default=0)
    haven = models.TextField(default='')
    operation = models.TextField(default='')
    summ = models.FloatField(default=0.0)
    transaction_date = models.TextField(default='')
    transaction_number = models.IntegerField(default=0)

    def __str__(self):
        return self.operation