from django.db import models
from django.template.defaultfilters import slugify


class Update(models.Model):

    title = models.CharField(max_length=127)
    published_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    slug = models.SlugField(max_length=127, blank=True, editable=False)
    link = models.URLField()
    link_text = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Update, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class UpdateImage(models.Model):

    image = models.ImageField()
    update = models.ForeignKey(Update, on_delete=models.CASCADE)


class Contact(models.Model):

    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    update = models.ForeignKey(Update, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
