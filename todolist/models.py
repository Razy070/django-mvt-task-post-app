from django.contrib.auth.models import User
from django.db import models


class ToDo(models.Model):
    title = models.CharField('Название задания', max_length=300)
    description = models.TextField('Описание', max_length=3000, editable=True, blank=True, default="")
    is_complete = models.BooleanField('Завершено', default=False)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return f"{self.title} ({self.id}) {self.description}"


class Post(models.Model):
    title = models.TextField()
    description = models.TextField('Описание', max_length=3000)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
