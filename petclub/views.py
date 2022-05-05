from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

class HelloWorld(APIView):

    def get(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Estoy en el get!", status=200) # respuesta del servicio

    def path(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        
        return Response(data="Estoy en el path !", status=200) # respuesta del servicio
    def delete(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint

        return Response(data="Estoy en el delete!", status=200) # respuesta del servicio
    def post(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Estoy en el post !", status=200) # respuesta del servicio