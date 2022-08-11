from django.db import models

SKINTYPES = (
    ('D', 'Dry'),
    ('C', "Combination"),
    ('O', 'Oily')
)
# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    skintype = models.CharField(
        max_length=1,
        choices=SKINTYPES,
        default=SKINTYPES[0][0]
    )
    def __str__(self):
        return self.name
