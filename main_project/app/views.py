from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Advert
from .serializers import AdvertSerializer


class AdvertListView(generics.ListAPIView):
    queryset = Advert.objects.select_related('city', 'category').all()
    serializer_class = AdvertSerializer


class AdvertDetailView(APIView):

    def get(self, request, advert_pk):
        advert = Advert.objects.select_related('city', 'category').get(pk=advert_pk)
        advert.views += 1
        advert.save()
        serializer = AdvertSerializer(advert)
        return Response(serializer.data)



