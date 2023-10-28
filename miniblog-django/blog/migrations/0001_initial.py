# Generated by Django 4.2.6 on 2023-10-26 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Bosh yozuv')),
                ('description', models.TextField(verbose_name='Teks yozuvu')),
                ('author', models.CharField(max_length=100, verbose_name='Muallif ismi')),
                ('date', models.DateField(verbose_name='Data Publikatsii')),
            ],
        ),
    ]