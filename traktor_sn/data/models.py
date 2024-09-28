from django.db import models
from django.utils import timezone

class Articles(models.Model):
    title = models.CharField('название', max_length=50)
    anons = models.CharField('анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата', default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural='новости'