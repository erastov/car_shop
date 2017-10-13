from django import forms
from .models import Customer, Employee, Order, Provider, Accessory, Car, MoreAboutOrder
import re
from django.core.exceptions import ValidationError

class CustomerForm(forms.ModelForm):

    def clean_fio(self):
        data = self.cleaned_data['fio']
        if not re.match(r'[A-Za-zА-Яа-яЁё\s]+$', data):
            raise ValidationError('Введите корректное ФИО')

        return data

    def clean_address(self):
        data = self.cleaned_data['address']
        if not re.match(r'[0-9A-Za-zА-Яа-яЁё\-\.\/\s]+$', data):
            raise ValidationError('Введите корректный адрес')

        return data

    def clean_tel(self):
        data = self.cleaned_data['tel']
        if not re.match(r'(\+?\d[- .]*){7,13}$', data):
            raise ValidationError('Введите корректный телефон')

        return data

    class Meta:
        model = Customer
        fields = '__all__'

        labels = {
            'fio': ('ФИО'),
            'address': ('Адрес'),
            'tel': ('Телефон'),
        }

        widgets = {
            'fio': forms.TextInput(attrs={'class':'form-control', 'aria-describedby':'basic-addon1'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'aria-describedby':'basic-addon1'}),
            'tel': forms.TextInput(attrs={'class':'form-control', 'aria-describedby':'basic-addon1', 'pattern': '(\+?\d[- .]*){7,13}'})
        }


class AccessoryForm(forms.ModelForm):

    def clean_name(self):
        data = self.cleaned_data['name']
        if not re.match(r'[A-Za-zА-Яа-яЁё\s]+$', data):
            raise ValidationError('Введите корректное название')

        return data


    class Meta:
        model = Accessory
        fields = '__all__'

        labels = {
            'name': ('Название'),
            'provider': ('Поставщик'),
            'price': ('Цена'),
            'count': ('Количество'),
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'aria-describedby':'basic-addon1'}),
            'provider': forms.Select(attrs={'class':'form-control', 'aria-describedby':'basic-addon1'}),
            'price': forms.TextInput(attrs={'class':'form-control', 'aria-describedby':'basic-addon1', 'type':'number', 'step':'0.01'}),
            'count': forms.TextInput(attrs={'class':'form-control', 'aria-describedby':'basic-addon1', 'type':'number'})
        }


class CarForm(forms.ModelForm):

    def clean_name(self):
        data = self.cleaned_data['name']
        if not re.match(r'[\dA-Za-zА-Яа-яЁё\s]+$', data):
            raise ValidationError('Введите корректное название')

        return data

    def clean_year(self):
        data = self.cleaned_data['year']
        if data < 1900 or data > 2017:
            raise ValidationError('Введите корректный год')

        return data

    class Meta:
        model = Car
        fields = ['name', 'type_engine', 'body', 'year', 'price', 'count']

        labels = {
            'name': ('Название'),
            'type_engine': ('Двигатель'),
            'body': ('Кузов'),
            'year': ('Год'),
            'price': ('Цена'),
            'count': ('Количество'),
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'aria-describedby':'basic-addon1'}),
            'type_engine': forms.Select(attrs={'class':'form-control', 'aria-describedby':'basic-addon1'}),
            'body': forms.Select(attrs={'class':'form-control', 'aria-describedby':'basic-addon1'}),
            'year': forms.TextInput(attrs={'class':'form-control', 'aria-describedby':'basic-addon1', 'type':'number'}),
            'price': forms.TextInput(attrs={'class':'form-control', 'aria-describedby':'basic-addon1', 'type':'number', 'step':'0.01'}),
            'count': forms.TextInput(attrs={'class':'form-control', 'aria-describedby':'basic-addon1', 'type':'number'})
        }