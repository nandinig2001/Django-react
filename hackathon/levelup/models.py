from django.db import models

# Create your models here.
class NewsArticle(models.Model):
    title=models.CharField(max_length=255)
    content = models.TextField()
    summary=models.TextField(blank=True, null=True)
    published_at=models.DateTimeField()

    def __str__(self):
        return self.title