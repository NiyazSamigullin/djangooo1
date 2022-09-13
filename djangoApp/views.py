from django.shortcuts import render
from models import Example
import random

def hello(request):
    context = {'var': random.randint(0, 100), 'var2': 'smth'}
    return render(request, 'hello.html', context = context)
def main(request):
    ex = Example()
    ex.smth = 100
    ex.smth2 = 'something'
    ex.save()

    return render(request, 'main.html')

def main(request):
    return render(request, 'main.html')
