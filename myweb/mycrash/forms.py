# -*- coding: utf-8 -*-
from django import forms
from mycrash import models

class ElementForm(forms.ModelForm):
    class Meta:
        model=models.Accident
        exclude=('pub_date',)
        # fields=['NAME','PEDS','PERNOTMVIT','VE_TOTAL','PVH_INVL','PERSONS','PERMVIT','CITY','MONTH','DAY','YEAR','NHS','ROUTE',
        #         'ROUTE1','TYP_INT','REL_ROAD','LGT_COND','WEATHER','ARR_HOUR','SFACTOR','DRUNK_DR','FATALS']

    # def __init__(self,*args,**kwargs):
    #     super(ElementForm,self).__init__(*args,**kwargs)
    #     self.fields['NAME'].label='名称'
    #     self.fields['PEDS'].label = 'PEDS'
    #     self.fields['NHS'].label = 'NHS'

class VehicleForm(forms.ModelForm):
    class Meta:
        model=models.VehicleData
        exclude=('',)

class PersonForm(forms.ModelForm):
    class Meta:
        model=models.PersonData
        exclude=('',)

class PhotoForm(forms.ModelForm):
    class Meta:
        model=models.Photo
        exclude=('',)