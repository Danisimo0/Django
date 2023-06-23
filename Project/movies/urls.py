from django.urls import path
from django.views.decorators.cache import cache_page
from django.conf import settings
from .views import CustomErrorView

from .models import Reviews, LikeDislike
from .views import (
    MoviesView,
    FilterMoviesView,
    SearchView,
    AboutUsView,
    FAQView,
    UserRegisterView,
    UserLoginView,
    LogoutUserView,
    CatalogView,
    VotesView,
    SingleMovieView,
    AddReview,
    ActorDetailView,
    DirectorDetailView,
)

cache_time = settings.CACHES

urlpatterns = [
    path('', cache_page(cache_time)(MoviesView.as_view()), name='home'),
    path('catalog/', cache_page(cache_time)(CatalogView.as_view()), name='catalog'),
    path('filter/', cache_page(cache_time)(FilterMoviesView.as_view()), name='filter'),
    path('search/', cache_page(cache_time)(SearchView.as_view()), name='search'),
    path('about/', cache_page(cache_time)(AboutUsView), name='about'),
    path('help/', cache_page(cache_time)(FAQView), name='help_page'),
    path('register/', cache_page(cache_time)(UserRegisterView.as_view()), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('catalog/<slug:slug>/', cache_page(cache_time)(CatalogView.as_view()), name='genre_catalog'),
    path('<slug:slug>/review/<int:pk>/like/', VotesView.as_view(model=Reviews, vote_type=LikeDislike.LIKE),
         name='review_like'),
    path('<slug:slug>/review/<int:pk>/dislike/', VotesView.as_view(model=Reviews, vote_type=LikeDislike.DISLIKE),
         name='review_dislike'),
    path('error/', CustomErrorView.as_view(), name='error'),
    path('<slug:slug>/', SingleMovieView.as_view(), name='movie_detail'),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review'),
    path('actor/<str:slug>/', cache_page(cache_time)(ActorDetailView.as_view()), name='actor_detail'),
    path('producer/<str:slug>/', cache_page(cache_time)(DirectorDetailView.as_view()), name='director_detail'),
]
