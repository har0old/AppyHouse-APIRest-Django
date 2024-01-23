from rest_framework.response import Response
from Appyhouselist_app.api.serializers import CommentSerializer, CompanySerializer, PropertySerializer, CommentAllSerializer
from Appyhouselist_app.models import Comment, Company, Property
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from Appyhouselist_app.api.permissions import AdminOrReadOnly, CommentUserOrReadOnly

class commentsCreate(generics.CreateAPIView):
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        return Comment.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        property = Property.objects.get(pk=pk)
        user = self.request.user
        comment_queryset = Comment.objects.filter(property=property, comment_user=user)
        if comment_queryset.exists():
            raise ValidationError("El usuario ya escribió un comentario para esta propiedad.")
        serializer.save(property = property, comment_user = user)
        
class commentsAll(generics.ListCreateAPIView):
    queryset= Comment.objects.all()
    serializer_class = CommentAllSerializer
    
class commentsList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Comment.objects.filter(property=pk)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CommentUserOrReadOnly]
    
# class CompanyVS(viewsets.ModelViewSet):
#      permission_classes = [IsAuthenticated]
#     queryset= Company.objects.all()
#     serializer_class = CompanySerializer

class CompanyVS(viewsets.ViewSet):
    permission_classes = [AdminOrReadOnly]
    def list(self, request):
        queryset = Company.objects.all()
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Company.objects.all()
        properties = get_object_or_404(queryset, pk=pk)
        serializer = CompanySerializer(properties)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = CompanySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def update(self, request, pk):
        try:        
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response({'error':'Empresa no encontrada'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        else: 
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
    def destroy(self, request, pk):
        try:        
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response({'error':'Empresa no encontrada'}, status=status.HTTP_400_BAD_REQUEST)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
                
class CompanyListAV(APIView):
    def get(self, request):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True, context={'request': request}) 
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CompanySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompanyDetailAV(APIView):
    def get(self, request, pk):
        try:        
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response({'Error':'Empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CompanySerializer(company, context={'request': request})
        return Response(serializer.data)
    
    def put(self,request, pk):
        try:        
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response({'Error':'Empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        else: 
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         
    def delete(self, request, pk):
        try:        
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response({'Error':'Empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PropertyListAV(APIView):
    def get(self, request):
        property = Property.objects.all()
        serializer = PropertySerializer(property, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PropertySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class PropertyDetailAV(APIView):
    def get(self, request, pk):
        try:        
            property = Property.objects.get(pk=pk)
        except Property.DoesNotExist:
            return Response({'Error':'Propiedad no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PropertySerializer(property)
        return Response(serializer.data)
    
    def put(self,request, pk):
        try:        
            property = Property.objects.get(pk=pk)
        except Property.DoesNotExist:
            return Response({'Error':'Propiedad no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PropertySerializer(property, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         
    def delete(self, request, pk):
        try:        
            property = Property.objects.get(pk=pk)
        except Property.DoesNotExist:
            return Response({'Error':'Propiedad no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        property.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
# class commentsList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset= Comment.objects.all()
#     serializer_class = CommentSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class CommentDetail(mixins.RetrieveModelMixin, generics.GenericAPIView): 
#     queryset= Comment.objects.all()
#     serializer_class = CommentSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    