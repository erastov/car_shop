from django.db import models

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    fio = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)

    def __str__(self):
        return str(self.fio)


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    fio = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    salary = models.FloatField(default=0)

    def __str__(self):
        return str(self.fio)


class Provider(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return str(self.name)

class Accessory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    provider = models.ForeignKey(Provider)
    count = models.IntegerField(null=True)

    def __str__(self):
        return str(self.name + ' ' + str(self.provider))


class Car(models.Model):
    TYPE_ENGINE_CHOICES = (
        ('БНЗ', 'Бензин'),
        ('ДЗЛ', 'Дизель'),
        ('ГБР', 'Гибрид'),
        ('ЭЛК', 'Электро'),
    )

    BODY_CHOICES = (
        ('СДН', 'Седан'),
        ('ХТЧ', 'Хэтчбек'),
        ('ВНД', 'Внедорожник'),
        ('УНВ', 'Универсал'),
        ('КУП', 'Купе'),
        ('МНВ', 'Минивэн'),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    type_engine = models.CharField(
        max_length=3,
        choices=TYPE_ENGINE_CHOICES,
        default='БНЗ',
    )

    body = models.CharField(
        max_length=3,
        choices=BODY_CHOICES,
        default='СДН',
    )
    year = models.PositiveSmallIntegerField(null=True)
    price = models.FloatField(default=0)
    count = models.IntegerField(null=True)
    image = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.name)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer)
    employee = models.ForeignKey(Employee)
    car = models.ForeignKey(Car)
    date = models.DateField(null=True)
    cost = models.FloatField(default=0)

    def __str__(self):
        return str(str(self.car) + ' ' + str(self.customer))


class MoreAboutOrder(models.Model):
    id = models.AutoField(primary_key=True)
    accessory = models.ForeignKey(Accessory)
    order = models.ForeignKey(Order)
    count = models.IntegerField(null=True)

    def __str__(self):
        return str(str(self.order) + ' ' + str(self.accessory))
