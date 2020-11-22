import pickle
import datetime as dt

from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response

from .models import Pets, Transactions


class PetCategory(generics.GenericAPIView):
    ''' круговая диаграмма по возрастам животных'''
    def get(self, request):
        cats_set = Pets.objects.all().filter(type_of_pet=1).values('date_of_birth', 'type_of_pet')
        dogs_set = Pets.objects.all().filter(type_of_pet=2).values('date_of_birth', 'type_of_pet')

        time_now = dt.date.today()

        cats = {'kitten':0, 'young':0, 'adult':0, 'elderly':0, 'old':0}
        dogs = {'puppy':0, 'young':0, 'adult':0}

        for item in cats_set:
            if (time_now-item['date_of_birth']).days <= 365:
                cats['kitten'] += 1
            elif (time_now-item['date_of_birth']).days <= 1095 and (time_now-item['date_of_birth']).days > 365:
                cats['young'] += 1
            elif (time_now-item['date_of_birth']).days <= 407 and (time_now-item['date_of_birth']).days > 1095:
                cats['adult'] += 1
            elif (time_now-item['date_of_birth']).days <= 5475 and (time_now-item['date_of_birth']).days > 407:
                cats['elderly'] += 1
            else:
                cats['old'] += 1

        for dog in dogs_set:
            if (time_now-dog['date_of_birth']).days <= 183:
                dogs['kitten'] += 1
            elif (time_now-dog['date_of_birth']).days <= 1460 and (time_now-item['date_of_birth']).days > 183:
                dogs['young'] += 1
            else:
                dogs['adult'] += 1
        
        return JsonResponse({'cats':cats, 'dogs':dogs})


class PetCard(generics.GenericAPIView):

    def post(self, request):
        model = pickle.load(open('heroes.sav', 'rb'))
        pet_data = []        
        pet = get_object_or_404(Pets, id=request.data['pet_id'])
        pets_donats = Transactions.objects.filter(pet_id=request.data['pet_id']).values('summ')
        
        if pet:
            if pet.race == 'Без породы':
                pet_data.append(0)
            else:
                pet_data.append(1)
            
            if pet.type_of_pet == 1:
                pet_data.append(0)
            else:
                pet_data.append(1)
            
            if pet.gender == 1:
                pet_data.append(0)
            else:
                pet_data.append(1)

            pet_data.append(pet.in_favorites)
            pet_data.append(pet.take_to_home)
            pet_data.append(pet.take_to_walk)

            if pets_donats:
                donates_to_pet = 0

                for item in pets_donats:
                    donates_to_pet += item['summ']
                
                pet_data.append(donates_to_pet)
                pet_data.append(len(pets_donats))
            else:
                donates_to_pet = 0

                pet_data.append(donates_to_pet)
                pet_data.append(0)

            result = model.predict_proba(pet_data)

        return JsonResponse({"percentage":f'{round(result[1], 3)*100}', "donats":donates_to_pet, "profile_link":pet.profile_link,
            "gender":pet.gender.gender, "type_of_pet":pet.type_of_pet.pets_type, 'id':pet.id, 'name':pet.name})
        

class HappyPet(generics.GenericAPIView):
    ''' отправка инфы о днях рождения pets - сегодня, week-pets в течении недели'''
    def get(self, request):
        pets = list(Pets.objects.filter(date_of_birth__day=dt.date.today().day, date_of_birth__month=dt.date.today().month).values('id', 'name'))
        days = [23, 24, 25, 26, 27, 28, 29, 30] # костыль. не хватило времени
        week_pets = list(Pets.objects.filter(date_of_birth__day__in=days, date_of_birth__month=dt.date.today().month).values('id', 'name'))
        return JsonResponse({"today":pets, "in week":week_pets})

    def options(self, request):
        pets = list(Pets.objects.filter(date_of_birth__day=dt.date.today().day, date_of_birth__month=dt.date.today().month).values('id', 'name'))
        days = [23, 24, 25, 26, 27, 28, 29, 30] # костыль. не хватило времени
        week_pets = list(Pets.objects.filter(date_of_birth__day__in=days, date_of_birth__month=dt.date.today().month).values('id', 'name'))
        return JsonResponse({"today":pets, "in week":week_pets})

class Popular(generics.GenericAPIView):
    ''' вывод списка популярных'''
    def get(self, request):
        all_pets = Pets.objects.all()
        low = list(all_pets.filter(in_favorites=0).values('id', 'name'))
        average = list(all_pets.filter(in_favorites__range=[1, 9]).values('id', 'name'))
        high = list(all_pets.filter(in_favorites__range=[10, 1000000000]).values('id', 'name'))
        return JsonResponse({"low":low[:10], "average":average[:10], "high":high[:10]})


def ping():
    return JsonResponse({'ping?':'pong'})