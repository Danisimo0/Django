from django.db.models import Count, Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions, status, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from movies.models import Actor, Category, Movie, Genre, Reviews, Rating, MovieShots, LikeDislike

from .serializers import *
from .service import MovieFilter


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewCreateSerializer


class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewCreateSerializer
    permission_classes = [permissions.IsAdminUser]

    def create(self, request):  # , *args, **kwargs
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer


class ActorsListView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorsListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'film_actor__title']


class ActorListView(generics.RetrieveUpdateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_object(self):
        try:
            return self.queryset.get(pk=self.kwargs['pk'])
        except Actor.DoesNotExist:
            raise NotFound('Actor not found.')


class GenreMoviesView(generics.ListAPIView):
    serializer_class = MovieListSerializer

    def get_queryset(self):
        genre_name = self.kwargs['genre_name']
        return Movie.objects.filter(genres__name__iexact=genre_name)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreListSerializer


class GenresListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenresListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class GenreListView(generics.RetrieveUpdateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreListSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_object(self):
        try:
            return self.queryset.get(name=self.kwargs['name'].title())
        except Genre.DoesNotExist:
            raise NotFound('Genre not found.')

    def update(self, request):  # , *args, **kwargs
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class MovieActorsView(generics.ListAPIView):
    serializer_class = ActorListSerializer

    def get_queryset(self):
        kinopoisk_id = self.kwargs['kinopoisk_id']
        movie = Movie.objects.get(kinopoisk_id=kinopoisk_id)
        return movie.actors.all()


class PopularMoviesView(generics.ListAPIView):
    serializer_class = MovieListSerializer

    def get_queryset(self):
        return Movie.objects.order_by('-rating')[:10]


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer


class MoviesListView(generics.ListAPIView):
    serializer_class = MoviesListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = MovieFilter
    search_fields = ['title']
    ordering_fields = ['year', 'rating']
    queryset = Movie.objects.all()


class MovieListView(generics.RetrieveUpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]

    def get_object(self):
        try:
            return self.queryset.get(kinopoisk_id=self.kwargs['kinopoisk_id'])
        except Movie.DoesNotExist:
            raise NotFound('Movie not found.')

    def update(self, request):  # , *args, **kwargs
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = ReviewSerializer


class MovieFilterBackend(DjangoFilterBackend):
    def filter_queryset(self, request, queryset):  # , view
        year = request.query_params.get('year')
        if year:
            queryset = queryset.filter(year=year)
        rating = request.query_params.get('rating')
        if rating:
            queryset = queryset.filter(rating__gte=rating)
        return queryset


class LatestMoviesView(generics.ListAPIView):
    serializer_class = MovieListSerializer

    def get_queryset(self):
        return Movie.objects.order_by('-release_date')[:10]


class MovieReviewsView(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        kinopoisk_id = self.kwargs['kinopoisk_id']
        return Reviews.objects.filter(movie__kinopoisk_id=kinopoisk_id)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesListSerializer


class CategoryMoviesView(generics.ListAPIView):
    serializer_class = MovieListSerializer

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        return Movie.objects.filter(category__name__iexact=category_name)


class CategoriesListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesListSerializer


class TopActorsView(generics.ListAPIView):
    serializer_class = ActorListSerializer

    def get_queryset(self):
        queryset = Actor.objects.annotate(movie_count=Count('movies'))
        queryset = queryset.annotate(avg_movie_rating=Avg('movies__rating'))
        queryset = queryset.order_by('-rating', '-movie_count', '-avg_movie_rating')[:10]
        return queryset


class TopRatedMoviesView(generics.ListAPIView):
    serializer_class = MovieListSerializer

    def get_queryset(self):
        return Movie.objects.order_by('-rating')[:10]
