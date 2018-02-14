from django.db import models

class Soal(models.Model):
    KUNCI_JAWABAN = (("A", "A"), ("B", "B"), ("C", "C"), ("D", "D"), ("E", "E"),)

    soal = models.TextField()
    kunci_jawaban = models.CharField(max_length=1, choices=KUNCI_JAWABAN)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return self.soal


class PilihanSoal(models.Model):
    JAWABAN = (("A", "A"), ("B", "B"), ("C", "C"), ("D", "D"), ("E", "E"),)

    soal = models.ForeignKey(Soal, related_name='pilihan', on_delete=models.CASCADE)
    pilihan = models.CharField(max_length=255)
    jawaban = models.CharField(max_length=1, choices=JAWABAN)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('soal',)
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return self.pilihan


class Konfigurasi(models.Model):
    BUKA = 1
    TUTUP = 0
    SIFAT = ((1, "Buka"), (0, "Tutup"),)
    HK = "HK"
    PP = "PP"
    K3 = "K3"
    KEGIATAN_BIMTEK = (
        (HK, "Hak Kekayaan Intelektual"),
        (PP, "Perlindungan Profesi"),
        (K3, "Keselamatan Kerja"),
    )

    sifat = models.SmallIntegerField(default=TUTUP, choices=SIFAT)
    kegiatan = models.CharField(max_length=2, default=None, choices=KEGIATAN_BIMTEK)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return self.kegiatan
