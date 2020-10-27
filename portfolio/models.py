from django.db import models


class App(models.Model):
    name = models.CharField(max_length=100, default='title test')
    description = models.CharField(max_length=250, default='test')
    image = models.ImageField(upload_to='portfolio/images', blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name

