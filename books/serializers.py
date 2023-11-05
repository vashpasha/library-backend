from rest_framework import serializers

from .models import Book, UserBookRelation


class BookSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'author', 'image')


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookInputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    author = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=255, required=False, allow_null=True)
    image = serializers.ImageField(required=False, allow_null=True)
    file = serializers.FileField(required=False, allow_null=True)

    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.author = validated_data.get('author', instance.author)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.file = validated_data.get('file', instance.file)
        instance.save()
        return instance


class UserBookRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBookRelation
        fields = '__all__'