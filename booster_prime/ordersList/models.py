from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse


PAYMENT_CHOICES = [
    ('cash', 'Наличные'),
    ('credit_card', 'Банковская карта'),
    ('bank_transfer', 'Онлайн перевод'),
    ('fuel_card', 'Топливная карта'),
]


class Fuel(models.Model):
    type = models.CharField('Топливо', max_length=50, db_index=True)
    price = models.DecimalField('Цена за литр', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Топливо'
        verbose_name_plural = 'Топливо'


class City(models.Model):
    name = models.CharField('Город', max_length=50, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Order(models.Model):
    orderNumber = models.AutoField('Номер заказа',primary_key=True)
    phoneNumber = PhoneNumberField('Номер телефона')
    name = models.CharField('Имя', max_length=50)
    carModel = models.CharField('Модель машины', max_length=50)
    carColor = models.CharField('Цвет машины', max_length=50)
    carNumber = models.CharField('Номер машины', max_length=10)
    fuel = models.ForeignKey(Fuel, on_delete=models.SET_NULL, null=True, verbose_name='Топливо')
    volume = models.IntegerField('Объем')
    totalPrice = models.IntegerField('Сумма', blank=0)
    paymentMethod = models.CharField('Способ оплаты',choices=PAYMENT_CHOICES, max_length=20)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, verbose_name='Город')
    address = models.CharField('Адрес', max_length=150)
    timeCreate = models.DateTimeField('Время создания заказа', auto_now_add=True)
    timeDeparture = models.DateTimeField('Время доставки')
    isDone = models.BooleanField('Выполнено', default=False)

    def __str__(self):
        return str(self.orderNumber)

    def save(self, *args, **kwargs):
        try:
            client = Client.objects.get(phoneNumber=self.phoneNumber)
        except ObjectDoesNotExist:
            client = Client(phoneNumber=self.phoneNumber, name=self.name, carModel=self.carModel, carColor=self.carColor, carNumber=self.carNumber, city=self.city, address=self.address)
            client.save()

        super(Order, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['timeCreate', 'timeDeparture']


class Client(models.Model):
    phoneNumber = PhoneNumberField('Номер телефона', primary_key=True)
    name = models.CharField('Имя', max_length=50)
    carModel = models.CharField('Модель машины', max_length=50)
    carColor = models.CharField('Цвет машины', max_length=50)
    carNumber = models.CharField('Номер машины', max_length=10)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, verbose_name='Город')
    address = models.CharField('Адрес', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['name']
