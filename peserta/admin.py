from django.contrib import admin
from django.db import models

from .models import Biodata

class BiodataAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informasi Personal', {'fields':
            ['user', 'nuptk', 'nama_lengkap', 'jenis_kelamin', 'nomor_hp', 'tempat_lahir', 'tanggal_lahir', 'asal_sekolah']}),
        ('Alamat', {'fields':
            ['kecamatan', 'kabupaten', 'provinsi']}),
    ]
    list_display = ('nama_lengkap', 'nuptk', 'asal_sekolah', 'kecamatan', 'kabupaten', 'provinsi')
    list_filter = ['kecamatan', 'kabupaten', 'provinsi']
    search_fields = ['nuptk', 'nama_lengkap', 'asal_sekolah']
    list_per_page = 10

admin.site.register(Biodata, BiodataAdmin)