from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=15)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name


class Song(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=15)
    date_released = models.DateField()
    likes = models.IntegerField()

    def __str__(self):
        return self.title


class Lyric(models.Model):
    Song = models.ForeignKey(Song, on_delete=models.PROTECT)
    content = models.CharField(max_length=500)
