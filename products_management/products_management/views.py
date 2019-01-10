from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse('hello')
    return render(request, 'home.html')

def product_add(request):
    return render(request, 'form.html')
def product_add_show(request):
    return render(request, 'product_add.html')
