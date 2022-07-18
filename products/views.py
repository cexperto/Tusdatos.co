from django.http import HttpResponse
from .models import Products
import pandas as pd
import json
import sqlite3

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required


def home(request):
    return HttpResponse('welcome to scrapy app, follow the readme file')

@login_required
def index(request):
    data = list(Products.objects.values())
    return JsonResponse(data, safe=False)

@login_required
def detaills(request, id):
    product = get_object_or_404(Products, pk=id)
    return render(request, 'products/detaill.html', {'product': product})

@login_required
def order(request, field):
    fields = ['index', 'titles', 'categories', 'price', 'description', 'images', 'reviews', 'ratings']
    if field not in fields:
        return JsonResponse({'error': 'field dont found'}, safe=False)
    products = Products.objects.all().order_by(field)[:5].values()    
    return JsonResponse({'data': list(products)}, safe=False)

@login_required
def load_csv(request):
    jf = json_formated()
    insert_df(jf)
    return HttpResponse('scrapy executed')
    

def json_formated():
    with open('ecommerce/products.json','r') as f:
            data = json.loads(f.read())
    
    categories = pd.json_normalize(data, record_path =['titles'],
    meta=[
        'categorie'
    ])
    price = pd.json_normalize(data, record_path =['price'])
    description = pd.json_normalize(data, record_path =['description'])
    images = pd.json_normalize(data, record_path =['images'])
    reviews = pd.json_normalize(data, record_path =['reviews'])
    ratings = pd.json_normalize(data, record_path =['ratings'])
    df = pd.concat([categories, price, description, images, reviews, ratings], axis=1)
    new_column_list = ['titles', 'categories', 'price', 'description', 'images', 'reviews', 'ratings']
    new_df=df.set_axis(new_column_list, axis=1)
    print(new_df)
    return new_df

def insert_df(df):
    conn = sqlite3.connect('db.sqlite3')
    df.to_sql('products', conn, if_exists='replace')
    
