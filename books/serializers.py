from rest_framework import serializers
from .models import Category, Country, Tag, Author, Book


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["id", "name"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class AuthorSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = Author
        fields = ["id", "name", "country"]


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        exclude = kwargs.pop('exclude', None)

        super().__init__(*args, **kwargs)

        if fields is not None:
            self.fields = {
                field: self.fields[field] for field in fields if field in self.fields
            }
        elif exclude is not None:
            exclude_set = set(exclude)
            for field_name in exclude_set:
                if field_name in self.fields:
                    self.fields.pop(field_name)

    class Meta:
        model = Book
        fields = ["id", "title", "author", "category", "tags"]
