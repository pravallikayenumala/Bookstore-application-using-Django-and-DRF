from rest_framework import serializers
from .models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author = Author.objects.create(**author_data)
        book = Book.objects.create(author=author, **validated_data)
        return book

    def update(self, instance, validated_data):
        author_data = validated_data.pop('author')
        author_serializer = AuthorSerializer(instance.author, data=author_data)
        author_serializer.is_valid(raise_exception=True)
        author = author_serializer.save()
        instance.author = author
        instance.title = validated_data.get('title', instance.title)
        instance.publisher = validated_data.get('publisher', instance.publisher)
        instance.publication_date = validated_data.get('publication_date', instance.publication_date)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
