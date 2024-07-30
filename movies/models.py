from django.db import models

class MovieReviewCache(models.Model):
    movie_id = models.IntegerField(unique=True)
    context = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MovieRecommendation(models.Model):
    movie_link = models.CharField(max_length=255, unique=True)
    movie_year = models.CharField(max_length=4)
    recommendations = models.JSONField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.movie_link} - Updated on {self.updated_at}"

    class Meta:
        app_label = 'movies'
