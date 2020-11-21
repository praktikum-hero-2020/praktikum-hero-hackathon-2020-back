from django.contrib import admin
from .models import City, Haven, Gender, PetsType, Pets, Transactions


class CityAdmin(admin.ModelAdmin):
    list_display = ('city_name',)
    fields = ('city_name',)


class HavenAdmin(admin.ModelAdmin):
    list_display = ('haven_name',)
    fields = ('haven_name',)

class GenderAdmin(admin.ModelAdmin):
    list_display = ('gender',)
    fields = ('gender',)

class PetsTypeAdmin(admin.ModelAdmin):
    list_display = ('pets_type',)
    fields = ('pets_type',)

class PetsAdmin(admin.ModelAdmin):
    list_display = ('name', 'haven', 'city', 'race','profile_link', 'type_of_pet', 'date_of_birth', 'gender', 'in_favorites', 'found_home', 'take_to_home', 'take_to_walk')
    fields = ('name', 'haven', 'city', 'race','profile_link', 'type_of_pet', 'date_of_birth', 'gender', 'in_favorites', 'found_home', 'take_to_home', 'take_to_walk')


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('pet_name', 'haven', 'summ', 'pet_id', 'operation', 'transaction_date', 'transaction_number')
    fields = ('pet_name', 'haven', 'summ', 'pet_id', 'operation', 'transaction_date', 'transaction_number')


admin.site.register(City, CityAdmin)
admin.site.register(Haven, HavenAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(PetsType, PetsTypeAdmin)
admin.site.register(Pets, PetsAdmin)
admin.site.register(Transactions, TransactionAdmin)