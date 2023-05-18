from django.db import models

class Anime(models.Model):
    title = models.CharField(max_length=100, null=False)
    text = models.CharField(max_length=5000, null=False)
    thumb = models.CharField(max_length=200, null=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    ep = models.IntegerField(null=False)
    srcMedium = models.CharField(max_length=5000, null=True)
    srcHD = models.CharField(max_length=5000, null=True)
    anime = models.ForeignKey(
        "animesDetails.AnimeDetails",
        on_delete=models.CASCADE,
        related_name="eps",
        null=True
    )
    

    

    def __repr__(self):
        return f"<[{self.title}]>"
