from rest_framework import serializers
from .models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    #author = AuthorSerializer()
    class Meta:
        model = Book
        fields = '__all__' # (includes all fields)
        # fields =  ['title', 'author']
        read_only_fields = ['id', 'owner'] 
        #use read_only_fields or ReadOnlyField for info the client should never supply
        # exclude (specifies fields to exclude)