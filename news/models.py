from django.db import models

# Create your models here.

class New(models.Model):
    title = models.CharField(max_length=100, null=False, unique = True)
    subtitle = models.CharField(max_length=100, default= ' ')
    text = models.CharField(max_length=5000, null=False)
    thumb = models.CharField(max_length=200, null=False)
    date = models.CharField(max_length=100, null=False, default= ' ')
    category = models.CharField(max_length=20, null=False, default= ' ' )

    def __repr__(self):
        return f"<[{self.title}]>"
