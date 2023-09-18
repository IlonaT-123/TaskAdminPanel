from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework import generics, status
from rest_framework.response import Response
from yookassa import Configuration, Payment

from booster_prime import settings
from .models import Fuel
from .serializers import FuelTypeSerializer, OrderCreateSerializer


class FuelTypeList(generics.ListAPIView):
    queryset = Fuel.objects.all()
    serializer_class = FuelTypeSerializer


class OrderCreate(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer

    def create(self, request, *args, **kwargs):
        Configuration.account_id = settings.YOOKASSA_SHOP_ID
        Configuration.secret_key = settings.YOOKASSA_SECRET_KEY

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return_url = reverse('success-page')
            order = serializer.instance
            if order.paymentMethod == 'credit_card':
                payment = Payment.create({
                    "amount": {
                        "value": str(order.totalPrice),
                        "currency": "RUB"
                    },
                    "description": f"Оплата заказа #{order.orderNumber}",
                    "confirmation": {
                        "type": "redirect",
                        "return_url": return_url,
                    }
                })

                return redirect(payment.confirmation.confirmation_url)
            else:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    return HttpResponse('Страница приложения')

def success(request):
    return HttpResponse('Платеж прошел')
