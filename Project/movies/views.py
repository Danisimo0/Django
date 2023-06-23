import logging
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import BaseCreateView
from movies.forms import ReviewForm, UserRegisterForm, UserLoginForm
from movies.models import Movie, Genre, Rating, Reviews, LikeDislike

logger = logging.getLogger(__name__)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class MoviesFilter:
    template_name = 'movies/filter.html'
    def get_genres(self):
        return Genre.objects.all().order_by('name')

    def get_years(self):
        return Movie.objects.values_list('year', flat=True).distinct().order_by('-year')

    def get_countries(self):
        return Movie.objects.values_list('country', flat=True).distinct().order_by('country')


class MoviesView(MoviesFilter, View):
    model = Movie
    template_name = 'movies/home.html'

    def get(self, request):
        carousel_movies = Movie.objects.order_by('kinopoisk_rating')[:12].prefetch_related('genres')
        premieres = Movie.objects.order_by('-world_premiere')[:8].prefetch_related('genres').select_related('category')
        new_movies = Movie.objects.order_by('-year')[:18].prefetch_related('genres')
        cartoon_id = Genre.objects.get(slug='multfilm')
        cartoons_list = Movie.objects.filter(genres=cartoon_id).order_by('-year')[:12].prefetch_related('genres')

        context = {
            'carousel_list': carousel_movies,
            'premieres_list': premieres,
            'cartoons_list': cartoons_list,
            'new_movies_list': new_movies
        }
        return render(request, self.template_name, context)


class FilterMoviesView(MoviesFilter, ListView):

    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()

        filter_params = self.request.GET

        title = filter_params.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title)

        director = filter_params.get('director')
        if director:
            queryset = queryset.filter(director__icontains=director)

        return queryset


class SearchView(MoviesFilter, ListView):
    template_name = 'movies/search_results.html'
    paginate_by = 12

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = Movie.objects.filter(
                Q(title__icontains=query) | Q(title_en__icontains=query) | Q(description__icontains=query)
            )
            return object_list
        return Movie.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context


class AboutUsView(View):
    def get(self, request):
        return render(request, 'movies/about_us.html')


class FAQView(View):
    def get(self, request):
        return render(request, 'movies/faq_page.html')


class UserRegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'movies/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('Invalid form!')


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'movies/login.html'


class LogoutUserView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class CatalogView(MoviesFilter, ListView):
    template_name = 'movies/catalog_movies.html'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()

        # Получаем параметры фильтрации из запроса
        min_rating = self.request.GET.get('min_rating')
        max_rating = self.request.GET.get('max_rating')

        # Применяем фильтры к queryset
        if min_rating is not None:
            queryset = queryset.filter(rating__gte=min_rating)

        if max_rating is not None:
            queryset = queryset.filter(rating__lte=max_rating)

        return queryset


class VotesView(View):
    model = Reviews
    vote_type = LikeDislike.LIKE

    def post(self, request, slug, pk):
        user = request.user
        action = request.POST.get('action')

        if user.is_authenticated:
            movie = get_object_or_404(Movie, slug=slug)
            try:
                likedislike = LikeDislike.objects.get(content_type=self.model, object_id=pk, user=user)
                if action == 'like':
                    likedislike.vote = LikeDislike.LIKE
                elif action == 'dislike':
                    likedislike.vote = LikeDislike.DISLIKE
                else:
                    likedislike.vote = None
                likedislike.save()
            except ObjectDoesNotExist:
                if action == 'like':
                    LikeDislike.objects.create(content_type=self.model, object_id=pk, user=user, vote=LikeDislike.LIKE)
                elif action == 'dislike':
                    LikeDislike.objects.create(content_type=self.model, object_id=pk, user=user,
                                               vote=LikeDislike.DISLIKE)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})


class SingleMovieView(MoviesFilter, DetailView, BaseCreateView):
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'
    form_class = ReviewForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movie_id = kwargs['object'].id
        context['reviews'] = Reviews.objects.filter(movie=movie_id, parent__isnull=True).all()
        context['review_children'] = Reviews.objects.filter(movie=movie_id, parent__isnull=False).all()
        context['recommended_films'] = Movie.objects.filter(
            genres__in=kwargs['object'].genres.all().values_list('pk').distinct())[:6]
        return context

    def mark_movie_as_viewed(self, movie_id):
        if self.request.user.is_authenticated:
            movie = get_object_or_404(Movie, pk=movie_id)
            self.request.user.watched_movies.add(movie)

    def get(self, request, *args, **kwargs):
        movie_id = kwargs.get('pk')
        self.mark_movie_as_viewed(movie_id)
        return super().get(request, *args, **kwargs)


class AddReview(View):

    def rating_counter(self, request, obj_id, action):
        obj_type = ContentType.objects.get_for_model(Reviews)
        try:
            obj = Rating.objects.get(content_type=obj_type, object_id=obj_id, user=request.user)
        except ObjectDoesNotExist:
            obj = Rating(content_type=obj_type, object_id=obj_id, user=request.user)

        if action == 'like':
            obj.vote = 1
        elif action == 'dislike':
            obj.vote = -1
        else:
            obj.vote = 0

        obj.save()

    def post(self, request, **kwargs):
        form = ReviewForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                form.instance.user = request.user
                form.instance.movie_id = kwargs['pk']
                form.save()
                return redirect('single_movie_url', kwargs['pk'])
            else:
                return redirect('login_url')

    def get(self, request):
        return redirect('/')


class ActorDetailView(MoviesFilter, DetailView):
    template_name = 'movies/actor_detail.html'
    context_object_name = 'actor'

    def get_queryset(self):
        queryset = super().get_queryset()

        filter_params = self.request.GET

        movie_title = filter_params.get('movie_title')
        if movie_title:
            queryset = queryset.filter(movies__title__icontains=movie_title)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = Movie.objects.filter(actors=self.kwargs['pk']).prefetch_related('genres')[:12]
        return context


class DirectorDetailView(MoviesFilter, DetailView):
    template_name = 'movies/director_detail.html'
    context_object_name = 'director'

    def get_queryset(self):
        queryset = super().get_queryset()

        filter_params = self.request.GET

        movie_title = filter_params.get('movie_title')
        if movie_title:
            queryset = queryset.filter(movies__title__icontains=movie_title)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = Movie.objects.filter(director=self.kwargs['pk']).prefetch_related('genres')[:12]
        return context


class CustomErrorView(View):
    def get(self, request, exception=None):
        exception_type = type(exception).__name__ if exception else None
        return render(request, 'errors/error.html', {'exception_type': exception_type})


def handler400(request, exception=None):
    exception_type = type(exception).__name__ if exception else None
    return render(request, 'errors/400.html', {'exception_type': exception_type}, status=400)


def handler403(request, exception=None):
    exception_type = type(exception).__name__ if exception else None
    return render(request, 'errors/403.html', {'exception_type': exception_type}, status=403)


def handler404(request, exception=None):
    exception_type = type(exception).__name__ if exception else None
    return render(request, 'errors/404.html', {'exception_type': exception_type}, status=404)


def handler500(request, exception=None):
    exception_type = type(exception).__name__ if exception else None
    return render(request, 'errors/500.html', {'exception_type': exception_type}, status=500)
