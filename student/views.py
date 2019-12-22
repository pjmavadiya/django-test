from django.shortcuts import render
import django_filters.rest_framework
from rest_framework import filters
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import AllowAny
from .models import *
from .serializers import *
import uuid 


class StudentAPI(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes = [AllowAny,]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['school', 'nationality']
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['first_name', 'last_name']

    def perform_create(self, serializer):
        serializer.save(s_id=uuid.uuid4().hex[:20].upper())


class SchoolAPI(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()
    permission_classes = [AllowAny,]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['city', 'state']
    search_fields = ['name',]
    ordering_fields = ['name',]


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    def get_queryset(self):
        return Student.objects.filter(school=self.kwargs['school_pk'])

    def perform_create(self, serializer):
        serializer.save(s_id=uuid.uuid4().hex[:20].upper())


