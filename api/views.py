from django.shortcuts import render
from django.http import JsonResponse

from products.models import Product
import json
# Create your views here.

def api_home(request, *args, **kwargs):
    # request -> HTTPRequest(instance) -> Django

    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price

        # need to serialize
        # model instance (model data)
        # turn a Python dict
        # return JSON to my client
    return JsonResponse(data)



    # first section
    # print("GET URL query param", request.GET)
    # print("POST URL query param", request.POST)
    #
    # body = request.body # byte string
    # try:
    #     data = json.loads(body)
    # except:
    #     pass
    #
    # data['headers'] = request.headers
    # data['content_type'] = request.content_type
    # print(data)
    # return JsonResponse({"message": "Hello World"})


