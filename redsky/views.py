from django.shortcuts import render

# Create your views here.

from .models import ProductDetails
import requests

def get_product_name(product_id):
    #here data is fetching from model, instead of this it can make a get request to the external url
    #code for calling external url
    '''
    url= "http://redsky.target.com/v2/pdp/tcin/"
    response = requests.get(url+product_id)
    data = response.json()
    if response.code==200:
      return {"id": product_id, "name": data.get("name")}
    else:
      return {}
    '''
    product = ProductDetails.objects.filter(product_id=product_id)
    if product.exists():
        return {"id": product_id, "name": product[0].product_name}
    else:
        return {}
