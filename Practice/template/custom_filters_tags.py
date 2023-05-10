from django import template
import random
from datetime import datetime

register = template.Library()


@register.filter(name='reverse_string')
def reverse_string(value):
    return value[::-1]


register = template.Library()


@register.simple_tag
def random_number(min_value=0, max_value=100):
    return


@register.filter(name='convert_date')
def convert_date(value):
    if isinstance(value, datetime):
        return value.strftime('%d-%m-%Y %H:%M')
    return value


@register.simple_tag(name='get_comment_count')
def get_comment_count(post):
    return post.comments.count()
