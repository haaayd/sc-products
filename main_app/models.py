from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

SKINTYPES = (
    ('D', 'Dry'),
    ('C', "Combination"),
    ('O', 'Oily')
)
HOWTO = (
    ('A', 'AM'),
    ('B', 'AM & PM'),
    ('P', 'PM')
)
# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField(max_length=250, default='My favorite thing about this product...')
    skin_type = models.CharField(
        max_length=1,
        choices=SKINTYPES,
        default=SKINTYPES[0][0]
    )
    time = models.CharField(
        max_length=1,
        choices=HOWTO,
        default=HOWTO[0][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('profiles_detail', kwargs={'profile_id': self.id})

