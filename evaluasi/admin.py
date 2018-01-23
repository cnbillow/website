from django.contrib import admin
from .models import Soal, Hasil, Saran, Konfigurasi

class SoalAdmin(admin.ModelAdmin):
    list_display = ('soal', 'jenis', 'created_at', 'updated_at')
    list_filter = ['created_at']
    search_fields = ['soal']
    list_per_page = 25

class HasilAdmin(admin.ModelAdmin):
    list_display = ('soal', 'created_at', 'updated_at')
    list_filter = ['created_at']
    search_fields = ['soal', 'jenis']
    list_per_page = 50

class SaranAdmin(admin.ModelAdmin):
    list_display = ('saran', 'kegiatan', 'created_at', 'updated_at')
    list_filter = ['created_at']
    search_fields = ['saran', 'kegiatan']
    list_per_page = 50

class KonfigurasiAdmin(admin.ModelAdmin):
    list_display = ('kegiatan', 'sifat', 'created_at', 'updated_at')
    list_filter = ['created_at', 'sifat', 'kegiatan']
    search_fields = ['kegiatan', 'sifat']
    list_per_page = 15

admin.site.register(Soal, SoalAdmin)
admin.site.register(Hasil, HasilAdmin)
admin.site.register(Saran, SaranAdmin)
admin.site.register(Konfigurasi, KonfigurasiAdmin)
