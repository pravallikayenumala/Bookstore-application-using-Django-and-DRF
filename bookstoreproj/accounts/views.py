from django.shortcuts import render
from django.conf import settings
from django.core.exceptions import ValidationError
#from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import  CreateModelMixin
from rest_framework.response import Response
from .serializers import customeruserserializer
from .serializers import Verifyserializer
from .twilio import send_otp_sms
import random
from rest_framework import generics
from.serializers import CustomTokenSerializer
from rest_framework_simplejwt import views
from myapp.serializers import AuthorSerializer
from myapp.models import Author
from rest_framework.views import APIView
 
#from rest_framework_simplejwt.authentication import JWTAuthentication


class Registrationview(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class=customeruserserializer

    def create(self, request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid()
        phone_number = request.data['phone_number']
        send_otp_sms(phone_number)
        
        serializer.save()
        
        return Response({'msg': 'success'})
    
class Verifyview(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class=Verifyserializer


    def post(self,request):
        phone_number=request.data.get('phone_number')
        otp = request.data.get('otp')
        try:
            user=CustomUser.objects.get(phone_number=phone_number,otp=otp)
            user.otp=''
            user.save()
        
            return Response({'otp verified sucessfull'})
        
        except CustomUser.DoesNotExist:
            raise  ValidationError
        
class LoginView(views.TokenObtainPairView):
    serializer_class = CustomTokenSerializer


    
class BookstoreprojListView(APIView):
    #authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        stu = Author.objects.all()
        serializer = AuthorSerializer(stu, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Posted'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors) #status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk = True, format = None):
        id = pk
        stu =Author.objects.get(id=id)
        serializer = AuthorSerializer(stu, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Posted'})
        return Response(serializer.error_messages)

    def patch(self, request, pk = True, format= None):
        id = pk
        stu = Author.objects.get(pk=id)
        serializer =AuthorSerializer(stu, data = request.data, partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':  'Data Posted'})
        return Response(serializer.errors)

    def delete(self, request, pk = True, format= None):
        id = pk
        stu = Author.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})

    





        
    




    
    
  
    

