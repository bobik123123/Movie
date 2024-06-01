from django.http.request import HttpRequest


from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination

from .models import Movie, Janr, Author
from .serializers import MovieSerializer, JanrSerializer, AuthorSerializer


class Welcome(APIView):

    def get(self, request: HttpRequest):
        return Response(data={'message': 'Hello, world!'})


class JanrList(GenericViewSet, ListModelMixin):
    pagination_class = LimitOffsetPagination
    queryset = Janr.objects.all()
    serializer_class = JanrSerializer


class MovieList(GenericViewSet, ListModelMixin):
    pagination_class = LimitOffsetPagination
    serializer_class = MovieSerializer
    def get_queryset(self):
        queryset = Movie.objects.all()
        janr = self.request.query_params.get('janr_id')
        author = self.request.query_params.get('author_id')
        if janr:
            return Movie.objects.filter(janr=janr)
        if author:
            return Movie.objects.filter(authors=author)
        if queryset:
            return queryset
        return "Не удалось найти"


class AuthourList(GenericViewSet, ListModelMixin):
    pagination_class = LimitOffsetPagination
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
