from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class ToDo(models.Model):
    title = models.CharField('Название задания', max_length=3000)
    is_complete = models.BooleanField('Завершено', default=False)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
