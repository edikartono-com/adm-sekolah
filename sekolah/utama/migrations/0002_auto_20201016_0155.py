# Generated by Django 3.0.8 on 2020-10-15 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utama', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='name',
            field=models.CharField(choices=[('ganjil', 'Ganjil'), ('genap', 'Genap')], max_length=10),
        ),
    ]
