# Generated by Django 3.1.3 on 2020-11-21 11:02

from datetime import datetime as dt
from django.db import migrations, models
import os
import csv
from pathlib import Path
from django.shortcuts import get_object_or_404


def get_cities(apps, schema_editor):
    City = apps.get_model('api', 'City')
    csv_pets=os.path.join('pets.csv')
    data_pets = csv.reader(open(csv_pets, encoding='utf-8'), delimiter = ',')
    cities = []
    for row in data_pets:
        cities.append(row[4])
    cities = list(set(cities))
    
    for item in cities:
        try:
            new = City(city_name=item)
            new.save()
        except:
            pass

def get_haven(apps, schema_editor):
    Haven = apps.get_model('api', 'Haven')
    csv_pets=os.path.join('pets.csv')
    data_pets = csv.reader(open(csv_pets, encoding='utf-8'), delimiter = ',')
    havens = []
    for row in data_pets:
        havens.append(row[3])
    havens = list(set(havens))
    for item in havens:
        try:
            new = Haven(haven_name=item)
            new.save()
        except:
            pass

def get_gender(apps, schema_editor):
    Gender = apps.get_model('api', 'Gender')
    csv_pets=os.path.join('pets.csv')
    data_pets = csv.reader(open(csv_pets, encoding='utf-8'), delimiter = ',')
    genders = []
    for row in data_pets:
        genders.append(row[8])
    genders = list(set(genders))
    for item in genders:
        try:
            new = Gender(gender=item)
            new.save()
        except:
            pass

def get_petstype(apps, schema_editor):
    PetsType = apps.get_model('api', 'PetsType')
    csv_pets=os.path.join('pets.csv')
    data_pets = csv.reader(open(csv_pets, encoding='utf-8'), delimiter = ',')
    pets_type = []
    for row in data_pets:
        pets_type.append(row[6])
    pets_type = list(set(pets_type))
    for item in pets_type:
        try:
            new = PetsType(pets_type=item)
            new.save()
        except:
            pass

def get_pets(apps, schema_editor):
    csv_pets=os.path.join('pets.csv')
    data_pets = csv.reader(open(csv_pets, encoding='utf-8'), delimiter = ',')
    
    City = apps.get_model('api', 'City')
    Haven = apps.get_model('api', 'Haven')
    Gender = apps.get_model('api', 'Gender')
    PetsType = apps.get_model('api', 'PetsType')
    
    Pets = apps.get_model('api', 'Pets')

    # for row in data_pets:
    try:
        obj_list = [
            Pets(
                id=row[0],
                name=row[1],
                profile_link=row[2],
                haven=get_object_or_404(Haven, haven_name=row[3]),
                city=get_object_or_404(City, city_name=row[4]),
                race=row[5],
                type_of_pet=get_object_or_404(PetsType, pets_type=row[6]),
                date_of_birth=row[7],
                gender=get_object_or_404(Gender, gender=row[8]),
                in_favorites=row[9],
                found_home=False if row[10] == '0' else True,
                take_to_home=row[11],
                take_to_walk=row[12]
            )
            for row in data_pets
        ] 
    except:
        pass
    Pets.objects.bulk_create(obj_list)


def get_transactions(apps, schema_editor):
    csv_trans=os.path.join('trans.csv')
    data_trans = csv.reader(open(csv_trans, encoding='utf-8'), delimiter = ',')

    Transactions = apps.get_model('api', 'Transactions')
    try:
        obj_list=[
            Transactions(
                pet_name=row[0],
                pet_id=row[1],
                haven=row[2],
                operation=row[3],
                summ=row[4],
                transaction_date=row[5],
                transaction_number=row[6]
            ) for row in data_trans
        ]
    except:
        pass
    Transactions.objects.bulk_create(obj_list)
    

# "Кличка питомца","ИД питомца","Название приюта","Название операции","Сумма операции","Дата","Номер заказа"
# Мадлен,1,"Самарский приют для животных ""НадеждА""","Игрушка для кошек ""Танцующая дразнилка""",95,2016-11-08 18:44:35,5944

#     pet_name = models.CharField(max_length=100)
#     pet_id = models.IntegerField(default=0)
#     haven = models.TextField(default='')
#     operation = models.TextField(default='')
#     summ = models.IntegerField(default=0)
#     transaction_date = models.DateTimeField(default=datetime.now())
#     transaction_number = models.IntegerField(default=0)
class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20201121_1627'),
    ]

    operations = [
        migrations.RunPython(get_cities),
        migrations.RunPython(get_haven),
        migrations.RunPython(get_gender),
        migrations.RunPython(get_petstype),
        migrations.RunPython(get_pets),
        migrations.RunPython(get_transactions),
    ]