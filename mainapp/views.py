from django.shortcuts import render

# Create your views here.
from django.views import View
from .forms import CurrencyPair
from currency_pasre import Currency

class IndexPageView(View):
    def get(self, request, *args, **kwargs):
        form = CurrencyPair()
        result = ''
        context = {
            'form': form,
            'result': result
            }

        return render(request, 'base.html', context)

    def post(self, request, *args, **kwargs):
        pass
