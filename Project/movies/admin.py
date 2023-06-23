from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Reviews, MovieShots, Actor, Category, Movie, Genre, Rating, LikeDislike


class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 0
    readonly_fields = ('name', 'movie', 'parent')


class MovieShortsInline(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110">')

    get_image.short_description = 'Photo'


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'country', 'kinopoisk_rating', 'year', 'slug')
    list_filter = ('category', 'kinopoisk_rating', 'year', 'genres', 'country')
    search_fields = ('title', 'category__name')
    readonly_fields = ('get_poster',)
    save_on_top = True
    inlines = [MovieShortsInline, ReviewInline]
    fields = (
        ('title', 'tagline', 'kinopoisk_id'), 'description', ('poster', 'get_poster'),
        ('year', 'world_premiere', 'country'),
        ('directors', 'actors', 'genres',),
        ('budget', 'fess_in_world',), ('kinopoisk_rating',), ('category', 'running_time'),
        ('slug', 'draft')
    )

    def get_poster(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="50" height="60">')

    get_poster.short_description = 'Poster'


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug', 'age')
    readonly_fields = ('get_image',)
    list_display_links = ('name', 'slug', 'age')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60">')

    get_image.short_description = 'Photo'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')
    search_fields = ('name',)


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('movie', 'name', 'ip', 'parent', 'rating')
    list_filter = ('parent', 'created_at', 'movie', 'rating')
    readonly_fields = ('movie', 'name', 'rating', 'parent')


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ('title', 'movie', 'get_image')
    list_filter = ('title', 'movie')
    search_fields = ('movie', 'title')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60">')

    get_image.short_description = 'Photo'


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('movie', 'avg_rating')
    readonly_fields = ('movie', 'avg_rating', 'count_reviews', 'sum_rating')


@admin.register(LikeDislike)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user_ip', 'content_object', 'object_id')













# from django.contrib import admin
# from django.utils.safestring import mark_safe
# from modeltranslation.admin import TranslationAdmin
#
# from .models import Reviews, MovieShots, Actor, Category, Movie, Genre, Rating, LikeDislike
#
#
# class ReviewInline(admin.TabularInline):
#     model = Reviews
#     extra = 0
#     readonly_fields = ('name', 'movie', 'parent')
#
#
# class MovieShortsInline(admin.TabularInline):
#     model = MovieShots
#     extra = 1
#     readonly_fields = ('get_image',)
#
#     def get_image(self, obj):
#         return mark_safe(f'<img src={obj.image.url} width="100" height="110">')
#
#     get_image.short_description = 'Photo'
#
#
# @admin.register(Movie)
# class MovieAdmin(TranslationAdmin):  # NEW: Изменено на TranslationAdmin
#     prepopulated_fields = {'slug': ('title',)}
#     list_display = ('title', 'category', 'country', 'kinopoisk_rating', 'year', 'slug')
#     list_filter = ('category', 'kinopoisk_rating', 'year', 'genres', 'country')
#     search_fields = ('title', 'category__name')
#     readonly_fields = ('get_poster',)
#     save_on_top = True
#     inlines = [MovieShortsInline, ReviewInline]
#     fields = (
#         ('title', 'tagline', 'kinopoisk_id'), 'description', ('poster', 'get_poster'),
#         ('year', 'world_premiere', 'country'),
#         ('directors', 'actors', 'genres',),
#         ('budget', 'fess_in_world',), ('kinopoisk_rating',), ('category', 'running_time'),
#         ('slug', 'draft')
#     )
#
#     def get_poster(self, obj):
#         return mark_safe(f'<img src={obj.poster.url} width="50" height="60">')
#
#     get_poster.short_description = 'Poster'
#
#
# @admin.register(Actor)
# class ActorAdmin(TranslationAdmin):  # NEW: Изменено на TranslationAdmin
#     prepopulated_fields = {'slug': ('name',)}
#     list_display = ('name', 'slug', 'age')
#     readonly_fields = ('get_image',)
#     list_display_links = ('name', 'slug', 'age')
#
#     def get_image(self, obj):
#         return mark_safe(f'<img src={obj.image.url} width="50" height="60">')
#
#     get_image.short_description = 'Photo'
#
#
# @admin.register(Genre)
# class GenreAdmin(TranslationAdmin):
#     prepopulated_fields = {'slug': ('name',)}
#     list_display = ('name', 'slug',)
#
#
# @admin.register(Category)
# class CategoryAdmin(TranslationAdmin):
#     prepopulated_fields = {'slug': ('name',)}
#     list_display = ('name', 'slug')
#     search_fields = ('name',)
#
#
# @admin.register(Reviews)
# class ReviewsAdmin(TranslationAdmin):
#     list_display = ('movie', 'name', 'ip', 'parent', 'rating')
#     list_filter = ('parent', 'created_at', 'movie', 'rating')
#     readonly_fields = ('movie', 'name', 'rating', 'parent')
#
#
# @admin.register(MovieShots)
# class MovieShotsAdmin(TranslationAdmin):
#     list_display = ('title', 'movie', 'get_image')
#     list_filter = ('title', 'movie')
#     search_fields = ('movie', 'title')
#     readonly_fields = ('get_image',)
#
#     def get_image(self, obj):
#         return mark_safe(f'<img src={obj.image.url} width="50" height="60">')
#
#     get_image.short_description = 'Photo'
#
#
# @admin.register(Rating)
# class RatingAdmin(admin.ModelAdmin):
#     list_display = ('movie', 'avg_rating')
#     readonly_fields = ('movie', 'avg_rating', 'count_reviews', 'sum_rating')
#
#
# @admin.register(LikeDislike)
# class LikeAdmin(admin.ModelAdmin):
#     list_display = ('user_ip', 'content_object', 'object_id')
