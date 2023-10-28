# Generated by Django 4.2.6 on 2023-10-26 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_img_alter_post_author_alter_post_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Запис', 'verbose_name_plural': 'Записи'},
        ),
        migrations.CreateModel(
            name='Coments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('text_comments', models.TextField(max_length=2000, verbose_name='Текс комментария')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='Пупликатсия')),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Коментарии',
            },
        ),
    ]
