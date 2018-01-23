from django.db import models

from peserta.models import Biodata


class Soal(models.Model):
    NS = "NS"
    PN = "PN"
    PL = "PL"
    TP = "TP"
    TIPE_SOAL = (
        (NS, "Narasumber"),
        (PN, "Panitia"),
        (PL, "Penyelenggara"),
        (TP, "Tempat Penyelenggara"),
    )

    soal = models.TextField()
    jenis = models.CharField(max_length=2, default=None, choices=TIPE_SOAL)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return self.soal


class Hasil(models.Model):
    HK = "HK"
    PP = "PP"
    K3 = "K3"
    KEGIATAN_BIMTEK = (
        (HK, "Hak Kekayaan Intelektual"),
        (PP, "Perlindungan Profesi"),
        (K3, "Keselamatan Kerja"),
    )
    SATU = 1
    DUA = 2
    TIGA = 3
    EMPAT = 4
    PILIHAN_NILAI = (
        (SATU, "Buruk"),
        (DUA, "Cukup"),
        (TIGA, "Baik"),
        (EMPAT, "Sangat Baik"),
    )

    peserta = models.ForeignKey(Biodata, on_delete=models.DO_NOTHING)
    soal = models.ForeignKey(Soal, on_delete=models.CASCADE)
    nilai = models.SmallIntegerField(default=None, choices=PILIHAN_NILAI)
    kegiatan = models.CharField(max_length=2, default=None, choices=KEGIATAN_BIMTEK)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return self.peserta.nama


class Saran(models.Model):
    HK = "HK"
    PP = "PP"
    K3 = "K3"
    KEGIATAN_BIMTEK = (
        (HK, "Hak Kekayaan Intelektual"),
        (PP, "Perlindungan Profesi"),
        (K3, "Keselamatan Kerja"),
    )

    peserta = models.ForeignKey(Biodata, on_delete=models.DO_NOTHING)
    saran = models.TextField()
    kegiatan = models.CharField(max_length=2, default=None, choices=KEGIATAN_BIMTEK)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return self.saran


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