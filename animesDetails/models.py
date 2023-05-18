from django.db import models

# Create your models here.

class AnimeDetails(models.Model):
    title = models.CharField(max_length=100, null=False, unique = True)
    text = models.CharField(max_length=5000, null=False)
    thumb = models.CharField(max_length=200, null=False)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f"<[{self.title}]>"
