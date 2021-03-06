# Generated by Django 4.0.5 on 2022-06-03 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyPairs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_currency_name', models.CharField(max_length=5, verbose_name='Первая валюта ')),
                ('second_currency_name', models.CharField(max_length=5, verbose_name='Название валюты')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, max_length=10, verbose_name='Цена к доллару')),
                ('last_time_update', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Currency',
        ),
    ]
