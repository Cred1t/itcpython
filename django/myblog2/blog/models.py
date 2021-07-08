from django.db import models
from django.db.models.deletion import CASCADE

class PostCategory(models.Model):
    name = models.CharField(max_length=255)
    link_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name 

class Post(models.Model):
    title = models.CharField(max_length=255)
    category_name = models.CharField(max_length=255)
    post_category = models.ForeignKey(PostCategory, on_delete=CASCADE)
    content = models.TextField()
    short_content = models.TextField()
    published = models.DateTimeField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title