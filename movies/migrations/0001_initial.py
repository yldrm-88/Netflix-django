# Generated by Django 5.0.4 on 2024-07-27 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filmismi', models.CharField(max_length=200, verbose_name='Film Adı')),
                ('aciklama', models.TextField(max_length=400, verbose_name='Açıklama')),
                ('resim', models.FileField(blank=True, null=True, upload_to='afis', verbose_name='Resim')),
            ],
        ),
    ]
