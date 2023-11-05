from django.db.models import Avg

from .models import UserBookRelation

def set_rating(book):
    rating = UserBookRelation.objects.filter(book=book).aggregate(rating=Avg('rate')).get('rating')
    book.rating=rating
    book.save()