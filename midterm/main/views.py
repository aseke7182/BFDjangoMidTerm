from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from rest_framework.response import Response
from rest_framework.permissions import *
from .serializers import *
from .models import *


class BookViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.ViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = (AllowAny,)
        else:
            permission_classes = (IsAdminUser,)
        return [permission() for permission in permission_classes]


class JournalViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.ViewSet):
    serializer_class = JournalSerializer
    queryset = Journal.objects.all()

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = (AllowAny,)
        else:
            permission_classes = (IsAdminUser,)
        return [permission() for permission in permission_classes]

