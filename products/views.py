from django.http import HttpResponse
# from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
# Create your views here.
def index(request):
    return HttpResponse('hey')

def detaills(request, id):
    return HttpResponse(id)

def load_csv(request):
    df = pd.read_csv('ecommerce/products.csv', header=None)
    print(df)
    return HttpResponse(df)

