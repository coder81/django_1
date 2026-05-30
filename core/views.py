from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

all_products = {
    "MacBook Air": {
      "price": 2000,
      "description": "CPU i7 Intel, 64 GB RAM, 1Tb Hard disc."
    },
    "iphone 16 Max Pro": {
      "price": 1300,
      "description": "Super phone, very fast!"
    },
    "Lenovo Laptop 3": {
      "price": 850,
      "description": "CPU i5 Intel, 16 GB RAM, 512Gb Hard disc."
    },
    "Asus Rog": {
      "price": 2500,
      "description": "CPU i9 Intel, 64 GB RAM, 2Tb Hard disc."
    },
    "ThinkPad T450": {
      "price": 980,
      "description": "CPU i7 Intel, 32 GB RAM, 1Tb Hard disc."
    }
  }

def home(request):
  context = {
    "all_products": all_products
  }
  return render(request, 'index.html', context)

def about(request):
  return HttpResponse("Shit heapens.", status=500)
def product(request, name):
  product = all_products.get(name)
  if not product:
    return HttpResponseNotFound("Product not found")

  # Prosledjivanje podataka u html
  context = {
    "product_name": name,
    "product_info": product
  }

  #return HttpResponse(f'Opis proizvoda: {name} - {product['price']} - {product['description']}')
  return render(request, 'product.html', context)

def user(request, userId):
  return HttpResponse(f'Ovo je korisnicki id: {userId}')