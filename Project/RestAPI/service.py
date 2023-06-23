from django_filters import rest_framework as filters
from rest_framework import filters as drf_filters, generics

from movies.models import Movie, Actor
from .serializers import MoviesListSerializer, ActorListSerializer


class CharListFilter(filters.BaseCSVFilter, filters.CharFilter):
    pass


class MovieFilter(filters.FilterSet):
    genres = CharListFilter(field_name='genres__name', lookup_expr='in')
    year = filters.RangeFilter()
    title = filters.CharFilter(lookup_expr='icontains')
    release_date = filters.DateFilter()

    class Meta:
        model = Movie
        fields = ['genres', 'year', 'title', 'release_date']


class CustomMoviesListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviesListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MovieFilter


class ActorsListView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer
    filter_backends = (drf_filters.SearchFilter,)  # Используем правильный модуль filters
    search_fields = ['name']
