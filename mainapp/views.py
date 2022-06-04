from django.shortcuts import render

# Create your views here.
from django.views import View
from .forms import CurrencyPairForm
from .currency_pasre import Currency, get_pair_json
from .exceptions import CantGetCurrencyData
from .models import *


class IndexPageView(View):
    def get(self, request, *args, **kwargs):
        form = CurrencyPairForm()
        result = ''
        context = {
            'form': form,
            'result': result
            }

        return render(request, 'base.html', context)

    def post(self, request, *args, **kwargs):
        form = CurrencyPairForm(request.POST)
        result = ''
        context = {
            'form': form,
            'result': result
        }
        if form.is_valid():
            currency_count, from_currency, to_currency = form.cleaned_data.values()
            print(currency_count, from_currency, to_currency)

            if from_currency == to_currency:
                context['same_currencies_error'] = True
                return render(request, 'base.html', context)

            try:
                get_pair_json(Currency[from_currency], Currency[to_currency])
            except CantGetCurrencyData:
                pass

            pair = CurrencyPair.objects.get(first_currency_name=from_currency, second_currency_name=to_currency)

            result = pair.price * currency_count

            context['result'] = result
            context['last_update_course'] = pair.last_time_update
            context['price'] = pair.price

        return render(request, 'base.html', context)
