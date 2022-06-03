from django.shortcuts import render

# Create your views here.
from django.views import View


class IndexPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html', {})

    def post(self, request, *args, **kwargs):
        pass
