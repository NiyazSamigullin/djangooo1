from django.shortcuts import render
import random
from djangoApp.models import Example
def hello(request):
    context = {'var': random.randint(0, 100), 'var2': 'smth'}
    return render(request, 'hello.html', context = context)
def main(request):
    context = {'from_db': Example.objects.all()[0].smth}

    return render(request, 'main.html', context=context)

