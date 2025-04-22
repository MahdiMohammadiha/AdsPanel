from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Ad, Service
from .serializers import AdSerializer, AdMinimalSerializer


def index(request):
    return render(request, "index.html")


class AdList(generics.ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdsByService(generics.ListAPIView):
    serializer_class = AdMinimalSerializer

    def get_queryset(self):
        service_id = self.kwargs["service_id"]
        service = get_object_or_404(Service, id=service_id)
        return Ad.objects.filter(services=service, is_active=True)
