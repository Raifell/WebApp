from django.db import models


class Article(models.Model):
    title = models.CharField('Title', max_length=255)
    announce = models.CharField('Announce', max_length=255)
    full_text = models.TextField('Text')
    date = models.DateField('Date')

    def __str__(self):
        return '{} - {} - {}'.format(self.id, self.title, self.date)
