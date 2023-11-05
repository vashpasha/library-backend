from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response

from .serializers import UserDetailSerializer, UserSmallSerializer
from books.models import Book, UserBookRelation
from books.serializers import BookSmallSerializer

UserModel = get_user_model()


class UserListAPI(APIView):
    def get(self, request):
        users = UserModel.objects.all()
        serializer = UserSmallSerializer(users, many=True)
        return Response(serializer.data)
    

class UserDetailAPI(APIView):
    def get(self, request):
        user = UserModel.objects.get(username=request.user.username)

        relations = UserBookRelation.objects.filter(user=user, in_bookmarks=True)
        ids = relations.values_list('book_id', flat=True)
        books = Book.objects.filter(pk__in=ids)

        user_books = user.userbookrelation_set.filter(in_bookmarks=True).values('book')
        serializer = UserDetailSerializer(user)
        book_serialzer = BookSmallSerializer(books, many=True)
        return Response({'user': serializer.data, 'books': book_serialzer.data})


#class UserDetailAPI(RetrieveUpdateAPIView):
 #   queryset = UserModel.objects.all()
  #  serializer_class = UserDetailSerializer
#
 #   def get_object(self):
  #      return self.queryset.get(user=self.request.user)