# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from mycrash.models import Accident,Photo,VehicleData,PersonData
from django.contrib import admin

# Register your models here.
class ElementAccidentAdmin(admin.ModelAdmin):
    list_display=('NAME','YEAR','MONTH','DAY')
    search_fields = ('YEAR','MONTH','DAY','CITY','NAME',)

class ElementVehicleAdmin(admin.ModelAdmin):
    list_display = ('NAME',)
    search_fields = ( 'NAME',)

class ElementPersonAdmin(admin.ModelAdmin):
    list_display = ('NAME',)
    search_fields = ('NAME',)

admin.site.register(Accident,ElementAccidentAdmin)
admin.site.register(VehicleData,ElementVehicleAdmin)
admin.site.register(PersonData,ElementPersonAdmin)
admin.site.register(Photo)
