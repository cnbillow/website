from django.db import models

from akun.models import User

class Biodata(models.Model):
    JENIS_KELAMIN_CHOICES = (("P", "Pria"),("W", "Wanita"))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nuptk = models.CharField(max_length=80)
    nama_lengkap = models.CharField(max_length=100)
    jenis_kelamin = models.CharField(max_length=1, default="P", choices=JENIS_KELAMIN_CHOICES)
    nomor_hp = models.CharField(max_length=13)
    tempat_lahir = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    asal_sekolah = models.CharField(max_length=100)
    kecamatan = models.CharField(max_length=6, null=True)
    kabupaten = models.CharField(max_length=4, null=True)
    provinsi = models.CharField(max_length=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return self.nama_lengkap