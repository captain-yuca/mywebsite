from django.db import models
from django.utils import timezone

class Project(models.Model):
    title= models.CharField(max_length=200)
    description=models.TextField()
    image_url=models.URLField()
    redirect_url=models.URLField()

    def as_json(self):
        return dict(
            id=self.id, title=self.title,
            description=self.description,
            image_url=self.image_url,
            redirect_url=self.redirect_url)
