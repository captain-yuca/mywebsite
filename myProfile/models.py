from django.db import models
from django.utils import timezone
from django.db.models import permalink

from .validators import validate_file_extension

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

class HomeInfo(models.Model):
        header = models.CharField(max_length=50)
        subheader = models.CharField(max_length=200)
        cv = models.FileField(upload_to='cv/', validators=[validate_file_extension])

        def as_json(self):
            return dict(
                header = self.header,
                subheader = self.subheader,
                cv = self.cv
                )


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    image = models.ImageField(upload_to = "blog/", default="blog/empty_post.jpg")
    category = models.ForeignKey('myProfile.Category')

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })
