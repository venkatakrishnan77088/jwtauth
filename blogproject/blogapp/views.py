from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer, BlogSerializer
from .models import Register
import jwt
import datetime


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'success': True,
            'msg': "account created successfully"
        })


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = Register.objects.filter(email=email, password=password).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not password:

            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow(),
            'name': user.username,
            'email': user.email,
            'gender': user.gender
        }

        #token = jwt.encode(payload, 'secret',algorithm='HS256').decode('utf-8')
        token = (jwt.encode(payload, 'secret', algorithm='HS256'))

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'Token': token
        }
        return response


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response


class CreatepostView(APIView):
    def post(self, request):
        #serializer = BlogSerializer(data=request.data)
        serializer = BlogSerializer(
            data=request.data, context={'request': request})

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'success': True,
            'msg': "blog created successfully"
        })
