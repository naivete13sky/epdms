import json
import os

from django import forms
from django.conf import settings
from django.contrib import admin
from .models import Profile,Customer


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'mobile','date_of_birth', 'photo']


class CustomerForm(forms.ModelForm):
    class Meta:
        widgets = {
            'country': forms.Select(),
            'province': forms.Select(),
            'city': forms.Select(),
        }

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    form = CustomerForm
    fields = ('name_full','name_simple','department','customer_type', ('country', 'province', 'city'))

    list_display = ['name_full', 'name_simple', 'department','province','city', 'customer_type', 'remark']
    search_fields = ('name_full', 'name_simple')

    def get_province_tuple(self):
        pass
        data = json.load(open(os.path.join(settings.BASE_DIR,r'account\china_region.json')))
        data_version = data['data_version']
        provinces = data['result'][0]
        provinces_tuple = ()
        for province in provinces:
            pass
            # print(province)
            # print(province["fullname"])
            provinces_tuple = provinces_tuple + ((province["id"], province["fullname"]),)
        print(provinces_tuple)
        # print(type(provinces_tuple))
        return provinces_tuple

    def get_region_dict(self):
        region_dict={}
        region_dict_china = {}
        data = json.load(open(os.path.join(settings.BASE_DIR,r'account\china_region.json')))
        data_version = data['data_version']
        provinces = data['result'][0]
        citys = data['result'][1]
        for province in provinces:
            pass
            # print(province["fullname"])

            cidx = province['cidx']
            province_citys_js = citys[cidx[0]:cidx[1]]
            one_province_city_list = []
            for city in province_citys_js:
                pass
                # print(city["fullname"])
                one_province_city_list.append(city["fullname"])
            region_dict_china[province["fullname"]] = one_province_city_list

        region_dict["??????"]=region_dict_china
        region_dict["??????"]={'??????': ['??????','??????','??????'],
                  '??????': ['??????','??????','??????','??????'],
                  '??????': ['??????','??????','??????','??????','??????','??????'],
                  '??????': ['??????','??????','??????','??????','??????','??????'],
                  '?????????': ['??????','??????','??????','??????','??????','?????????']}
        return region_dict

    #??????add_view??????????????????????????????????????????change_form.html????????????
    def add_view(self, request,  extra_context=None):
        extra_context = extra_context or {}
        extra_context['region_dict'] = self.get_region_dict()

        return super(CustomerAdmin, self).add_view(
            request,extra_context=extra_context,
        )