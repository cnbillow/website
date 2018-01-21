from django.db import models

# SIFAT = ((1, "Buka"),(0, "Tutup"),)
# KEGIATAN_BIMTEK = (
#     ("HK", "Hak Kekayaan Intelektual"),
#     ("PP", "Perlindungan Profesi"),
#     ("K3", "Keselamatan "),
# )

class SoalTest(models.Model):
    KUNCI_JAWABAN = (("A", "A"),("B", "B"),("C", "C"),("D", "D"),("E", "E"),)

    soal = models.TextField()
    kunci_jawaban = models.CharField(max_length=1, default="A", choices=KUNCI_JAWABAN)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return self.soal


class PilihanSoalTest(models.Model):
    KUNCI_JAWABAN = (("A", "A"),("B", "B"),("C", "C"),("D", "D"),("E", "E"),)

    soal = models.ForeignKey(SoalTest, on_delete=models.CASCADE)
    pilihan = models.CharField(max_length=255)
    jawaban = models.CharField(max_length=1, default="A", choices=KUNCI_JAWABAN)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return self.pilihan