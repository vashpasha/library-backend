from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import GenericViewSet


from .models import Book, UserBookRelation
from .serializers import BookDetailSerializer, BookSmallSerializer, UserBookRelationSerializer, BookInputSerializer


class BookListAPI(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSmallSerializer(books, many=True)
        return Response(serializer.data)
    

class BookDetailAPI(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book.objects.all(), pk=pk)
        serializer = BookDetailSerializer(book)
        return Response(serializer.data)
    

class BookCreateAPI(APIView):
    permission_classes=(IsAdminUser, )

    def post(self, request):
        book = request.data
        serializer = BookInputSerializer(data=book)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

class BookUpdateAPI(APIView):
    permission_classes=(IsAdminUser, )
    
    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), pk=pk)
        serializer = BookInputSerializer(book, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class BookDeleteAPI(APIView):
    permission_classes=(IsAdminUser, )

    def delete(self, request, pk):
        book = get_object_or_404(Book.objects.all(), pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class UserBookRelationAPI(APIView):
    def post(self, request):
        user = request.user
        book_id = request.data.get('book_id')

        user_book_relation, created = UserBookRelation.objects.get_or_create(user=user, book_id=book_id)

        if 'rate' in request.data:
            rate = request.data.get('raiting')        
            if rate is not None:
                user_book_relation.rate = rate
        
        if 'in_bookmarks' in request.data:
            in_bookmarks = request.data.get('in_bookmarks')   
            if in_bookmarks is not None:
                user_book_relation.in_bookmarks = in_bookmarks

        user_book_relation.save()

        serializer = UserBookRelationSerializer(user_book_relation)
        return Response(status=status.HTTP_201_CREATED)

    def put(self, request):
        user = request.user
        book_id = request.data.get('book_id')

        user_book_relation = get_object_or_404(UserBookRelation.objects.all(), user=user, book_id=book_id)

        if 'rate' in request.data:
            rate = request.data.get('raiting')        
            if rate is not None:
                user_book_relation.rate = rate
        
        if 'in_bookmarks' in request.data:
            in_bookmarks = request.data.get('in_bookmarks')   
            if in_bookmarks is not None:
                user_book_relation.in_bookmarks = in_bookmarks

        user_book_relation.save()

        serializer = UserBookRelationSerializer(user_book_relation)
        return Response(status=status.HTTP_200_OK)

    def delete(self, request):
        user = request.user
        book_id = request.data.get('book_id')

        user_book_relation = get_object_or_404(UserBookRelation.objects.all(), user=user, book_id=book_id)

        user_book_relation.rate = None 
        user_book_relation.in_bookmarks = False
        user_book_relation.save()

        serializer = UserBookRelationSerializer(user_book_relation)
        return Response(status=status.HTTP_200_OK)
