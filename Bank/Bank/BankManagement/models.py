from django.db import models


# Create your models here.
class Register(models.Model):
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password1 = models.CharField(max_length=120)
    password2 = models.CharField(max_length=120)

    @staticmethod
    def get_all_Register():
        return Register.objects.all()

    class Meta:
        verbose_name_plural="Register"


class Currency(models.Model):
    COUNTRY = models.CharField(max_length=30)
    CURRENCY = models.CharField(max_length=30)
    SYMBOL = models.CharField(max_length=30)
    QTY = models.CharField(max_length=30)
    PRICE = models.CharField(max_length=30)

    @staticmethod
    def get_all_currency():
        return Currency.objects.all()

    class Meta:
        verbose_name_plural="Currency"