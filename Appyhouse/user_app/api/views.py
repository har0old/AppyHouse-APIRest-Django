from rest_framework.decorators import api_view
from rest_framework.response import Response
from user_app.api.serializers import RecordSerializer
from rest_framework.authtoken.models import Token
#from user_app import models
from rest_framework import status 
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST',])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RecordSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
           account = serializer.save()
           data['response'] = 'El registro del usuario fue exitoso.'
           data['username'] = account.username
           data['email'] = account.email
           refresh = RefreshToken.for_user(account)
           data['token'] = {
               'refresh':str(refresh),
               'access':str(refresh.access_token)
           }
           #token = Token.objects.get(user=account).key
           #data['token'] = token 
        else:
            data = serializer.errors 
        return Response(data)