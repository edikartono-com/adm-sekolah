# Generated by Django 3.0.8 on 2020-10-24 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karyawan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='alias',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='gender',
            field=models.CharField(choices=[('wanita', 'Wanita'), ('pria', 'Pria')], default='pria', max_length=10),
        ),
        migrations.AlterField(
            model_name='staff',
            name='status_sekarang',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10),
        ),
    ]