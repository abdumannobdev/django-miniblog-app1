from django.db import models

# Create your models here.
class Post(models.Model):
    '''Malumot o yozish'''
    title = models.CharField('Заголовок записи', max_length=100)
    description = models.TextField('техт записи')
    author = models.CharField('Имя автора', max_length=100)
    date = models.DateField('Дата публикатсии')
    img = models.ImageField('изображения',upload_to='image/%Y')


    def __str__(self):
        return f'{self.title},{self.author}'


    class Meta:
        verbose_name = 'Запис'
        verbose_name_plural = 'Записи'

class Comments(models.Model):
    """коментарй"""
    email = models.EmailField()
    name = models.CharField('Имя',  max_length=50)
    text_comments = models.TextField('Текс комментария', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Пупликатсия', on_delete=models.CASCADE)
    

    def __str__(self):
        return f'{self.name},{self.post}'


    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
        
class Likes(models.Model):
    """Likes"""
    ip = models.CharField('Ip-adress', max_length=100)
    pos = models.ForeignKey(Post, verbose_name='Publikatsiya', on_delete=models.CASCADE)
    