from django.db import models

class News(models.Model):
    title = models.CharField(max_length=300)
    link = models.URLField(unique=True)
    content = models.TextField()
    media = models.CharField(max_length=100)
    crawled_at = models.DateTimeField(auto_now_add=True)