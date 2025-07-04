from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializers
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import viewsets

@api_view(['POST'])
@permission_classes([AllowAny])

def register(request):
    print(request.data)
    serializer = UserSerializers(data = request.data)
    if serializer.is_valid():
        serializer.save()
        user =  CustomUser.objects.get(username=serializer.data['username'])
        user.set_password(request.data['password'])    
        user.save()    
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
@permission_classes([AllowAny])

def login(request):
    user = get_object_or_404(CustomUser,username=request.data['username'])
    if user.activo == False:
        return Response({'error': 'Usuario no valido'},status=status.HTTP_400_BAD_REQUEST)
    if not user.check_password(request.data['password']):
        return Response({'error': 'Contraseña invalida'},status=status.HTTP_400_BAD_REQUEST)
    refresh = RefreshToken.for_user(user)
    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    },status=status.HTTP_200_OK)

class UsersViews(viewsets.ModelViewSet):
    serializer_class = UserSerializers
    def get_queryset(self):
     queryset = CustomUser.objects.filter(activo = True)
     eliminado = self.request.query_params.get('eliminados')
     if eliminado: 
        queryset = CustomUser.objects.all()
     return queryset
# Create your views here.
