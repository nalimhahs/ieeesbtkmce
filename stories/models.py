from django.db import models
from django.template.defaultfilters import slugify

class Story(models.Model):

    title = models.CharField(max_length=127)
    published_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    slug = models.SlugField(max_length=127, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Story, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class StoryImage(models.Model):

    image = models.ImageField()
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
