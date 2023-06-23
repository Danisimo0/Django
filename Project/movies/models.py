from datetime import date
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Sum
from django.urls import reverse


class Actor(models.Model):
    name = models.CharField("Name", max_length=100)
    age = models.PositiveSmallIntegerField("Age", default=0)
    description = models.TextField("Description", blank=True)
    image = models.ImageField("Image", upload_to="actors/", blank=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self, page=1):
        return reverse('actor_detail', kwargs={"slug": self.slug, 'page': page})

    class Meta:
        verbose_name = "Actors and directors"
        verbose_name_plural = "Actors and directors"


class Director(models.Model):
    name = models.CharField("Name", max_length=100)
    age = models.PositiveSmallIntegerField("Age", default=0)
    description = models.TextField("Description", blank=True)
    image = models.ImageField("Image", upload_to="directors/", blank=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self, page=1):
        return reverse('director_detail', kwargs={"slug": self.slug, 'page': page})

    class Meta:
        verbose_name = "Director"
        verbose_name_plural = "Directors"


class Category(models.Model):
    name = models.CharField("Category", max_length=150)
    description = models.TextField("Description", blank=True)
    slug = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Genre(models.Model):
    name = models.CharField("Name", max_length=100)
    description = models.TextField("Descriptions", blank=True)
    slug = models.SlugField(max_length=160, unique=True)

    def get_absolute_url(self, page=1):
        return reverse('genre_catalog', kwargs={'slug': self.slug, 'page': page})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"


class Movie(models.Model):
    title = models.CharField("Name", max_length=100)
    tagline = models.CharField("Tagline", max_length=100, blank=True, default='')
    kinopoisk_id = models.IntegerField('Kinopoisk ID', default=0, unique=True)
    description = models.TextField("Descriptions")
    poster = models.ImageField("Poster", upload_to="movies/")
    year = models.PositiveSmallIntegerField("Release date", default=2019)
    country = models.CharField("Country", max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name="Directors", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="Actors", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="Genres")
    world_premiere = models.DateField("World Premiere", default=date.today)

    kinopoisk_rating = models.FloatField(verbose_name='Rating Kinopoisk', default=0)
    running_time = models.FloatField('Duration', default=0)
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Draft", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.slug})

    def get_review(self):
        return self.reviews.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"


class MovieShots(models.Model):
    title = models.CharField("Title", max_length=100)
    description = models.TextField("Description", blank=True)
    image = models.ImageField("Image", upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name="Movie", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Movie Shot"
        verbose_name_plural = "Movie Shots"


class Rating(models.Model):
    count_reviews = models.IntegerField('Review Count', default=0)
    sum_rating = models.BigIntegerField('Star Count', default=0)
    avg_rating = models.FloatField('Average Rating', default=0)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Movie", related_name="ratings")

    def __str__(self):
        return f"{self.avg_rating} - {self.movie}"

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"


class Reviews(models.Model):
    ip = models.CharField("IP Address", max_length=15, default=0)
    name = models.CharField("Name", max_length=100)
    text = models.TextField("Message", max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')
    rating = models.IntegerField('User Rating', blank=True, default=0)
    parent = models.ForeignKey('self', verbose_name="Parent", on_delete=models.SET_NULL, blank=True, null=True,
                               related_name='children')
    movie = models.ForeignKey(Movie, verbose_name="Movie", on_delete=models.CASCADE, related_name='reviews')
    votes = GenericRelation('LikeDislike', related_query_name='reviews')

    def __str__(self):
        return f"{self.movie} - {self.name}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"


class LikeDislikeManager(models.Manager):
    use_for_related_fields = True

    def likes(self):
        return self.get_queryset().filter(vote__gt=0)

    def dislikes(self):
        return self.get_queryset().filter(vote__lt=0)

    def sum_rating(self):
        return self.get_queryset().aggregate(Sum('vote')).get('vote__sum') or 0


class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1

    VOTES = (
        (DISLIKE, 'Dislike'),
        (LIKE, 'Like')
    )

    vote = models.SmallIntegerField(verbose_name="Vote", choices=VOTES)
    user_ip = models.CharField("IP Address", max_length=15, default=0)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    objects = LikeDislikeManager()

    class Meta:
        verbose_name = "Like & Dislike"
        verbose_name_plural = "Likes & Dislikes"


class ErrorLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    error_type = models.CharField(max_length=100)
    error_message = models.TextField()

    def __str__(self):
        return f'{self.error_type} - {self.timestamp}'
