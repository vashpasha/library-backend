from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.CharField(max_length=225, null=True)

    image = models.ImageField(upload_to='covers', blank=True, null=True)
    file = models.FileField(null=True)

    raiting = models.DecimalField(max_digits=3, decimal_places=2, null=True)

    def __str__(self):
        return f'id:{self.id} {self.name} by {self.author}'


class UserBookRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    RATE_CHOICES = (
        (1, '1'), 
        (2, '2'), 
        (3, '3'), 
        (4, '4'), 
        (5, '5')
    )

    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null=True)
    in_bookmarks = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} relate with {self.book}'
    
    def save(self, *args, **kwargs):
        from .logic import set_rating

        creating = not self.pk
        old_rate = self.rate

        super().save(*args, **kwargs)

        if creating or self.rate != old_rate:
            set_rating(self.book)

    class Meta:
        unique_together = ['user', 'book']