from rest_framework import generics
from .models import Ad
from .serializers import AdSerializer


class AdDetailView(generics.RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    lookup_field = 'ad_id'
