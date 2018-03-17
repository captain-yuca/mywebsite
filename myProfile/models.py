from django.db import models
from django.utils import timezone

class Project(models.Model):
    title= models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to = "projects/", default="projects/empty_project.jpg" )
    redirect_url=models.URLField()

    def as_json(self):
        return dict(
            id=self.id, title=self.title,
            description=self.description,
            image=self.image,
            redirect_url=self.redirect_url)

class AboutInfo(models.Model):
        description=models.TextField()
        image=models.ImageField(upload_to = "about/", default="about/default.jpg" )
        last_updated=models.DateField(auto_now=True)

        def as_json(self):
            return dict(
                description=self.description,
                image=self.image,
                last_updated=self.last_updated
                )

class AboutUpToInfo(models.Model):
        description=models.TextField()


        def as_json(self):
            return dict(
                description=self.description
                )
