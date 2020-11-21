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
    name = models.CharField(max_length=100) # имя питомца
    profile_link = models.TextField(default='') # ссылка на профиль
    haven = models.ForeignKey(Haven, on_delete=models.CASCADE, related_name='pets_haven') # приют
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='pets_city') # город
    race = models.CharField(max_length=100) # порода
    type_of_pet = models.ForeignKey(PetsType, on_delete=models.CASCADE, related_name='pet_type') # кошка/собака
    date_of_birth = models.DateField(default='01.01.0000') # дата рождения
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name='pet_gender') # пол
    in_favorites = models.IntegerField(default=0) # в избранном
    found_home = models.BooleanField(default=False) # нашел дом
    take_to_home = models.IntegerField(default=0) # забрать домой
    take_to_walk = models.IntegerField(default=0) # погулять

    def __str__(self):
        return self.name


class Transactions(models.Model):
    pet_name = models.CharField(max_length=100) # имя питомца
    pet_id = models.IntegerField(default=0) # id питомца
    haven = models.TextField(default='') # приют
    operation = models.TextField(default='') # название операции
    summ = models.FloatField(default=0.0) # сумма операции
    transaction_date = models.TextField(default='') # дата операции 
    transaction_number = models.IntegerField(default=0) # номер операции 

    def __str__(self):
        return self.operation