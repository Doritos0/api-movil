import json
from django.http import JsonResponse
from django.shortcuts import redirect, render

from .models import Usuario, Viaje, ViajeTomado
from .serializers import UsuarioSerializer, ViajeSerializer, ViajeTomadoSerializer

# CREACION DE API
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser


from django.core.mail import send_mail




# Create your views here.

@csrf_exempt
@api_view(['GET','POST'])
def lista_usuarios(request):
    if request.method == 'GET':
        query = Usuario.objects.all()
        serializer = UsuarioSerializer(query, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        
        serializer = UsuarioSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            user = request.POST.get('user', None)
            print(user)
            if user in Usuario.objects.values_list('user', flat=True):
                print("ingresao")
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def detalle_usuarios (request,id):
    try:
        usuario = Usuario.objects.get(user=id)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serilizer = UsuarioSerializer(usuario)
        return Response(serilizer.data)
    if request.method == 'PUT':
        serilizer = UsuarioSerializer(usuario,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        else:
            return Response(serilizer.errors,status=status.HTTP_404_NOT_FOUND)
    if request.method =='DELETE':
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

@api_view(['GET','POST'])
def lista_viaje(request):
    if request.method == 'GET':
        query = Viaje.objects.all()
        serializer = ViajeSerializer(query, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        
        serializer = ViajeSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            patente = request.POST.get('patente', None)
            print(patente)
            if patente in Viaje.objects.values_list('patente', flat=True):
                print("ingresao")
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def detalle_viaje (request,id):
    try:
        viaje = Viaje.objects.get(patente=id)
    except Viaje.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serilizer = ViajeSerializer(viaje)
        return Response(serilizer.data)
    if request.method == 'PUT':
        serilizer = ViajeSerializer(viaje,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        else:
            return Response(serilizer.errors,status=status.HTTP_404_NOT_FOUND)
    if request.method =='DELETE':
        viaje.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    
@api_view(['GET','POST'])
def viajeTomado (request):
    if request.method == 'GET':
        query = ViajeTomado.objects.all()
        serializer = ViajeTomadoSerializer(query, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        
        serializer = ViajeTomadoSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            usuario = serializer.validated_data.get('usuario')
            viaje = serializer.validated_data.get('viaje')
            
            existe_registro = ViajeTomado.objects.filter(usuario=usuario, viaje=viaje).exists()

            if existe_registro:
                return Response({"error": "Ya existe un registro para este usuario y viaje."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])
def detalle_viaje_tomado (request,id):
    try:
        viaje = ViajeTomado.objects.get(id_viaje=id)
    except ViajeTomado.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serilizer = ViajeTomadoSerializer(viaje)
        return Response(serilizer.data)
    if request.method == 'PUT':
        serilizer = ViajeTomadoSerializer(viaje,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        else:
            return Response(serilizer.errors,status=status.HTTP_404_NOT_FOUND)
    if request.method =='DELETE':
        viaje.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

@api_view(['POST'])
@csrf_exempt
def enviar_correo(request):
    if request.content_type == 'application/json':
        data = json.loads(request.body)
        destinatario = data.get('destinatario')
        asunto = data.get('asunto')
        cuerpo = data.get('cuerpo')
    elif request.content_type == 'multipart/form-data':
        destinatario = request.POST.get('destinatario')
        asunto = request.POST.get('asunto')
        cuerpo = request.POST.get('cuerpo')
    else:
        return JsonResponse({'error': 'Formato de solicitud no soportado'}, status=400)

    try:
        send_mail(
            asunto,
            cuerpo,
            'tellevoapp01@gmail.com',
            [destinatario],
            fail_silently=False,
        )
        return JsonResponse({'mensaje': 'Correo enviado con éxito'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    

