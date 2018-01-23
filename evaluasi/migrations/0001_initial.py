# Generated by Django 2.0.1 on 2018-01-23 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('peserta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hasil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nilai', models.SmallIntegerField(choices=[(1, 'Buruk'), (2, 'Cukup'), (3, 'Baik'), (4, 'Sangat Baik')], default=None, max_length=1)),
                ('kegiatan', models.CharField(choices=[('HK', 'Hak Kekayaan Intelektual'), ('PP', 'Perlindungan Profesi'), ('K3', 'Keselamatan Kerja')], default=None, max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('peserta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='peserta.Biodata')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Konfigurasi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sifat', models.SmallIntegerField(choices=[(1, 'Buka'), (0, 'Tutup')], default=0, max_length=1)),
                ('kegiatan', models.CharField(choices=[('HK', 'Hak Kekayaan Intelektual'), ('PP', 'Perlindungan Profesi'), ('K3', 'Keselamatan Kerja')], default=None, max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Saran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saran', models.TextField()),
                ('kegiatan', models.CharField(choices=[('HK', 'Hak Kekayaan Intelektual'), ('PP', 'Perlindungan Profesi'), ('K3', 'Keselamatan Kerja')], default=None, max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('peserta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='peserta.Biodata')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Soal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soal', models.TextField()),
                ('jenis', models.CharField(choices=[('NS', 'Narasumber'), ('PN', 'Panitia'), ('PL', 'Penyelenggara'), ('TP', 'Tempat Penyelenggara')], default=None, max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
            },
        ),
        migrations.AddField(
            model_name='hasil',
            name='soal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluasi.Soal'),
        ),
    ]
