from rest_framework import serializers
from tes.models import Soal, PilihanSoal

class SoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soal
        fields = (
            'pk',
            'soal',
            'kunci_jawaban',
        )
        read_only_fields = ('created_at', 'updated_at')