from django.db import models

# Create your models here.


class CurrencyPair(models.Model):
    first_currency_name = models.CharField(max_length=5, verbose_name='Первая валюта ')
    second_currency_name = models.CharField(max_length=5, verbose_name='Название валюты')
    price = models.DecimalField(max_length=10, max_digits=10, decimal_places=2, verbose_name='Цена к доллару')
    last_time_update = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.first_currency_name} - {self.second_currency_name}"
