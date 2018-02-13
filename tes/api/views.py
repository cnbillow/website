from rest_framework import generics

from tes.models import Soal
from .serializers import SoalSerializer

class SoalView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = SoalSerializer

    def get_queryset(self):
        return Soal.objects.all()