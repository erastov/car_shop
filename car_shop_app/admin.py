from django.contrib import admin
from car_shop_app.models import Customer, Employee, Order, Provider, Accessory, Car, MoreAboutOrder

admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Order)
admin.site.register(Provider)
admin.site.register(Accessory)
admin.site.register(Car)
admin.site.register(MoreAboutOrder)
