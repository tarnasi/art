from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Post Title", max_length=80)
    content = models.TextField(verbose_name="Post Content")
    photo = models.ImageField(blank=True, null=True, upload_to="blogs/")
    created_at = models.DateTimeField(verbose_name="Post Published Date", auto_now_add=True)


    class Meta:
        ordering = ['-created_at']
    

    def __str__(self):
        return self.title
