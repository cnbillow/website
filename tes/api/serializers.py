from rest_framework import serializers
from tes.models import Soal, PilihanSoal

class SoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soal
        fields = ('pk', 'kegiatan', 'soal', 'kunci_jawaban',)
        read_only_fields = ('created_at', 'updated_at')

class PilihanSoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PilihanSoal
        fields = ('pilihan', 'jawaban',)
        read_only_fields = ('created_at', 'updated_at')

class SoalDetailSerializer(serializers.ModelSerializer):
    pilihan = PilihanSoalSerializer(many=True, read_only=True)

    class Meta:
        model = Soal
        fields = ('pk', 'kegiatan', 'soal', 'kunci_jawaban', 'pilihan',)
        read_only_fields = ('created_at', 'updated_at')