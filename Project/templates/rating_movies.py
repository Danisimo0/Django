from django import template
from django.shortcuts import get_object_or_404
from movies.models import Rating

register = template.Library()


@register.simple_tag
def get_movie_rating(movie_id):
    rating = get_object_or_404(Rating, movie_id=movie_id)
    return rating.avg_rating


@register.filter
def correct_num(num):
    return '{:,.0f}'.format(num).replace(',', ' ')
