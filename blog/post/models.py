from django.db import models
from ckeditor.fields import RichTextField

    
class BlogPost(models.Model):
    post_title = models.CharField(max_length=255)
    post_thumbnail = models.ImageField(blank=True, null=True, upload_to='images/')
    post_para = models.CharField(max_length=255, default='mani')
    post_created = models.DateTimeField(auto_now_add=True)
    post_updated = models.DateTimeField(auto_now=True)
    body = RichTextField()
    
    def __str__(self):
        return self.post_title
