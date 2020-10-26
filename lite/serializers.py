from rest_framework import serializers
from lite.models import Author,Reader

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'age', 'gender', 'signature']

class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = ['id', 'name', 'age', 'gender']