from django.urls import path
from rest_framework import routers
from django.urls import include
from . import views

router = routers.DefaultRouter()
router.register(r'actors', views.ActorViewSet)
router.register(r'genres', views.GenreViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'movies', views.MovieViewSet)
router.register(r'reviews', views.ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('movie/<int:kinopoisk_id>/', views.MovieDetailView.as_view()),
    path('movie/<int:kinopoisk_id>/reviews/', views.MovieReviewsView.as_view()),
    path('movie/<int:kinopoisk_id>/actors/', views.MovieActorsView.as_view()),
    path('actors/top/', views.TopActorsView.as_view()),
    path('genres/<int:pk>/movies/', views.GenreMoviesView.as_view()),
    path('categories/<int:pk>/movies/', views.CategoryMoviesView.as_view()),
    path('movies/popular/', views.PopularMoviesView.as_view()),
    path('movies/latest/', views.LatestMoviesView.as_view()),
    path('movies/top-rated/', views.TopRatedMoviesView.as_view()),
]

