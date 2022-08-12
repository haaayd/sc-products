from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

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

    def get_absolute_url(self):
        return reverse('profiles_detail', kwargs={'profile_id': self.id})
        
    user = models.ForeignKey(User, on_delete=models.CASCADE)
