from django.db import models

# Create your models here.

class QuestionsDb(models.Model):
    title = models.CharField(max_length=100)

    LANGUAGE_CHOICES =(
        ("python", "Python"),
        ("java","Java"),
        ("javascript","JavaScript")
    )

    language = models.CharField(max_length=100, choices= LANGUAGE_CHOICES, default= "python")

    DIFFICULTY_CHOICES = (
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard")
    )

    difficulty_levels = models.CharField(max_length=100, choices=DIFFICULTY_CHOICES, default= "easy")
    topic = models.CharField(max_length=200)
    notes =models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    sample_input = models.TextField()
    sample_output = models.TextField()
    is_active = models.BooleanField(default=True)
    score = models.IntegerField()
