# from modeltranslation.translator import register, TranslationOptions
# from .models import Category, Actor, Movie, Genre, MovieShots, Reviews, Rating, LikeDislike
#
#
# @register(Category)
# class CategoryTranslationOptions(TranslationOptions):
#     fields = ('name', 'description')
#
#
# @register(Actor)
# class ActorTranslationOptions(TranslationOptions):
#     fields = ('name', 'description')
#
#
# @register(Genre)
# class GenreTranslationOptions(TranslationOptions):
#     fields = ('name', 'description')
#
#
# @register(Movie)
# class MovieTranslationOptions(TranslationOptions):
#     fields = ('title', 'description', 'country')
#
#
# @register(MovieShots)
# class MovieShotsTranslationOptions(TranslationOptions):
#     fields = ('title', 'description')
#
#
# @register(Reviews)
# class ReviewsTranslationOptions(TranslationOptions):
#     fields = ('name',)
#
#
# @register(Rating)
# class RatingTranslationOptions(TranslationOptions):
#     fields = ('avg_rating',)
#
#
# @register(LikeDislike)
# class LikeDislikeTranslationOptions(TranslationOptions):
#     fields = ('user_ip',)
