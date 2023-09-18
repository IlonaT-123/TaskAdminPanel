from django.contrib import admin
from .models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ('orderNumber', 'fuel', 'volume', 'city', 'timeDeparture', 'timeCreate', 'isDone')
    list_editable = ('isDone',)
    list_filter = ('isDone', 'city', 'timeDeparture')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phoneNumber', 'city', 'carModel', 'carColor', 'carNumber')
    list_filter = ('city', 'carModel')


class FuelAdmin(admin.ModelAdmin):
    list_display = ('type', 'price')


admin.site.register(Order, OrderAdmin)
admin.site.register(Fuel, FuelAdmin)
admin.site.register(City)
admin.site.register(Client, ClientAdmin)

admin.site.site_title = 'Панель администратора Booster Prime'
admin.site.site_header = 'Панель администратора Booster Prime'
