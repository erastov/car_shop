from .models import Customer, Employee, Order, Provider, Accessory, Car, MoreAboutOrder
import django_filters


class CarFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Car
        fields = ['name', 'type_engine', 'body', 'year', 'price']