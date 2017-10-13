from django.shortcuts import render
import sqlite3
from django.http import HttpResponseRedirect
from .models import Customer, Employee, Order, Provider, Accessory, Car, MoreAboutOrder
from .forms import CustomerForm, AccessoryForm, CarForm
from django.shortcuts import get_object_or_404
from .filters import CarFilter


def customers_new(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect('/customers/')
    else:
        form = CustomerForm()
    return render(request, 'car_shop_app/customers_new_edit.html', {'form': form})


def customers_edit(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect('/customers/')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'car_shop_app/customers_new_edit.html', {'form': form})


def accessories_new(request):
    if request.method == "POST":
        form = AccessoryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect('/accessories/')
    else:
        form = AccessoryForm()
    return render(request, 'car_shop_app/accessories_new_edit.html', {'form': form})


def accessories_edit(request, id):
    accessory = get_object_or_404(Accessory, id=id)
    if request.method == "POST":
        form = AccessoryForm(request.POST, instance=accessory)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect('/accessories/')
    else:
        form = AccessoryForm(instance=accessory)
    return render(request, 'car_shop_app/accessories_new_edit.html', {'form': form})


def cars_new(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect('/cars/')
    else:
        form = CarForm()
    return render(request, 'car_shop_app/cars_new_edit.html', {'form': form})


def cars_edit(request, id):
    car = get_object_or_404(Car, id=id)
    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect('/cars/')
    else:
        form = CarForm(instance=car)
    return render(request, 'car_shop_app/cars_new_edit.html', {'form': form})


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def index(request):
 """Домашняя страница приложения Learning Log"""
 return render(request, 'car_shop_app/index.html')


def show(request, entity):
    """Просмотр"""
    con = sqlite3.connect("db.sqlite3")
    con.row_factory = dict_factory
    cursor = con.cursor()

    templates = {'cars': 'car_shop_app/cars.html', 
            'accessories': 'car_shop_app/accessories.html',
            'customers': 'car_shop_app/customers.html',
            }

    sql = {'accessories': ("SELECT acs.id as id, acs.name as name, prv.name as provider, price, count "
    	                   "FROM car_shop_app_accessory acs "
                           "INNER JOIN car_shop_app_provider prv ON acs.provider_id = prv.id"),
            'customers': ("SELECT * FROM car_shop_app_customer"),
            }

    if entity != 'cars':
        cursor.execute(sql[entity])
        rows = cursor.fetchall()
        context = {'values': rows}
    else:
        cars = Car.objects.all()
        cars_filter = CarFilter(request.GET, queryset=cars)
        context = {'values': cars_filter}
    
    return render(request, templates[entity], context)


def delete(request, id, entity):
    """Удаление сотрудника"""
    con = sqlite3.connect("db.sqlite3")
    con.row_factory = dict_factory
    cursor = con.cursor()

    sql = {'cars': ("DELETE "
                       "FROM car_shop_app_car "
                       "WHERE id = " + str(id)), 
            'accessories': ("DELETE "
                       "FROM car_shop_app_accessory "
                       "WHERE id = " + str(id)),
            'customers': ("DELETE "
                          "FROM car_shop_app_customer "
                          "WHERE id = " + str(id)),
            }
    cursor.execute(sql[entity])

    con.commit()
    return HttpResponseRedirect('/' + entity)