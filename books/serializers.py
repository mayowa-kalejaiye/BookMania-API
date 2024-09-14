from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

        def validate_isbn(self, value):
            if len(value) != 10 and len(value) != 13:
                raise serializers.ValidatationError("ISBN should be either 10 or 13 characters.")
            return value
