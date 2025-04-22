from django.shortcuts import render
from rest_framework import generics
from .models import Ad
from .serializers import AdSerializer


def index(request):
    return render(request, "index.html")


class AdList(generics.ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

class AdDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
