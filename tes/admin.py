from django.contrib import admin
from .models import Soal, PilihanSoal


class PilihanSoalInline(admin.TabularInline):
    model = PilihanSoal
    extra = 4


class SoalAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Soal Test', {'fields': ['soal', 'kunci_jawaban']}),
    ]
    inlines = [PilihanSoalInline]
    list_display = ('soal', 'kunci_jawaban', 'created_at', 'updated_at')
    list_filter = ['created_at']
    search_fields = ['soal']
    list_per_page = 25


admin.site.register(Soal, SoalAdmin)
