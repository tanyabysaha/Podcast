from django.db import models
from django.utils import timezone
from froala_editor.fields import FroalaField


class Podcast(models.Model):
    pod_title = models.CharField(max_length=200)
    description = FroalaField(null=True)
    long_description = FroalaField(null=True)
    audio = models.FileField(null=True)
    picture = models.ImageField(default="static/podcast/img/default.png")
    banner = models.ImageField(default="static/podcast/img/default.png")
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.pod_title

class Comment(models.Model):
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE, related_name="comments")
    user = models.CharField(max_length=200)
    comment_text = models.TextField()

    def __str__(self):
        return self.comment_text