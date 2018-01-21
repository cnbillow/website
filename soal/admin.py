from django.contrib import admin

from .models import SoalTest, PilihanSoalTest


class PilihanSoalTestInline(admin.TabularInline):
    model = PilihanSoalTest
    extra = 4


class SoalTestAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Soal Test', {'fields': ['soal', 'kunci_jawaban']}),
    ]
    inlines = [PilihanSoalTestInline]
    list_display = ('soal', 'kunci_jawaban', 'created_at', 'updated_at')
    list_filter = ['created_at']
    search_fields = ['soal']
    list_per_page = 25


admin.site.register(SoalTest, SoalTestAdmin)
