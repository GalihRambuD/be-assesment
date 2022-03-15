from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(blank=True, max_length=255)
    content = models.CharField(null=True, max_length=255)
    published_at = models.DateTimeField(blank=True, auto_now=True)
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)

    class Meta:
        managed = True
        db_table = 'posts'
