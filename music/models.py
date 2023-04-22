from django.db import models

# Create your models here.
class Songs(models.Model):
    title = models.CharField(max_length=255, null=False)
    artist = models.CharField(max_length=255, null=False)

    class Meta:
        verbose_name_plural = 'songs'

    def __str__(self):
        return f'{self.title} - {self.artist}'
