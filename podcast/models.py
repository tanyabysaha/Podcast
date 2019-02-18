from django.db import models
from django.utils import timezone
from froala_editor.fields import FroalaField



class Podcast(models.Model):
    pod_title = models.CharField(max_length=200)
    description = FroalaField()
    audio = models.FileField()
    picture = models.ImageField(default="static/podcast/img/Screen Shot 2019-02-11 at 6.29.29 PM.png")


    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.pod_title




