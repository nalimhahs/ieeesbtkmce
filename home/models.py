from django.db import models


class Awards(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title


class Carousel(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=50)
    link = models.URLField()

    def __str__(self):
        return self.title


class Society(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()

    def __str__(self):
        return self.name
