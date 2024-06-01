from rest_framework import serializers
from .models import Movie, Janr, Author

class JanrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Janr
        fields = ('id', 'name')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'middle_name', 'full_name')

class MovieSerializer(serializers.ModelSerializer):
    janr = JanrSerializer()
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('id', 'name', 'description', 'janr', 'authors', 'avatar', 'main_artists', 'artists', 'created_at')
