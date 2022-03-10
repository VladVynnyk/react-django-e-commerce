from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from .products import products


# Create your views here.
#It's view in django
#api_view(['GET'])
# def getRoutes(request):
#     routes = [
#         '/api/products',
#         '/api/products/create',
#
#         '/api/products/upload',
#
#         '/api/products/<id>/reviews',
#
#         '/api/products/top/',
#         '/api/products/<id>/',
#
#         '/api/products/delete/<id>/',
#         '/api/products/<update>/<id>/',
#     ]
#     return JsonResponse(routes, safe=False)
#


#And that is view in django_rest
@api_view(['GET'])
# @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def getRoutes(request):
    routes = [
        '/api/products',
        '/api/products/create',

        '/api/products/upload',

        '/api/products/<id>/reviews',

        '/api/products/top/',
        '/api/products/<id>/',

        '/api/products/delete/<id>/',
        '/api/products/<update>/<id>/',
    ]
    return Response(routes)

@api_view(['GET'])
def getProducts(request):
    return Response(products)

@api_view(['GET'])
def getProduct(request, pk):
    product = None
    for i in products:
        if i['_id']==pk:
            product = i
            break
    return Response(product)