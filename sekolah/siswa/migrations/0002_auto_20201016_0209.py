# Generated by Django 3.0.8 on 2020-10-15 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siswa', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='siswa',
            old_name='tangga_lahir',
            new_name='tanggal_lahir',
        ),
    ]