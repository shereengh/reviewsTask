from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Review(models.Model):
    title = models.CharField(max_length=120)
    rating = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )
    review = models.TextField()
    favorite = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
