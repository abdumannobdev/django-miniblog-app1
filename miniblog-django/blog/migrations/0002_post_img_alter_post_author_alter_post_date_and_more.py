# Generated by Django 4.2.6 on 2023-10-26 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='img.jpg', upload_to='image/%Y', verbose_name='изображения'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=100, verbose_name='Имя автора'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(verbose_name='Дата публикатсии'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(verbose_name='техт записи'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок записи'),
        ),
    ]