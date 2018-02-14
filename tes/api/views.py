from rest_framework import generics

from tes.models import (
    Soal,
    PilihanSoal,
    Konfigurasi,
)

from .serializers import (
    SoalSerializer,
    SoalDetailSerializer,
    PilihanSoalSerializer,
)

class SoalView(generics.ListAPIView):
    serializer_class = SoalSerializer

    def get_queryset(self):
        return Soal.objects.all()

class SoalDetailView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = SoalDetailSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Soal.objects.filter(pk=pk)

class SoalKegiatanView(generics.ListAPIView):
    lookup_field = 'kegiatan'
    serializer_class = SoalDetailSerializer

    def get_queryset(self):
        kegiatan = self.kwargs['kegiatan']
        return Soal.objects.filter(kegiatan=kegiatan).order_by('?')[5:]