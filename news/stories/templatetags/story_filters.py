# -*- coding:utf-8 -*-

from django.utils.timezone import utc
from django import template
from datetime import datetime

register = template.Library()


def numberWord125(value, word1, word2, word5):
    result = value % 100
    if result in xrange(11, 20):
        return word5
    result = value % 10
    if result == 1:
        return word1
    if result in xrange(2, 5):
        return word2
    return word5


@register.filter(name='age')
def age(created):
	now = datetime.utcnow().replace(tzinfo=utc)
	age_in_minutes = int((now - created).total_seconds()) / 60

	if age_in_minutes < 60:
		value = age_in_minutes
		precision = numberWord125(value, 'минута', 'минуты', 'минут')
	elif age_in_minutes < 60 * 24:
		value = age_in_minutes // 60
		precision = numberWord125(value, 'час', 'часа', 'часов')
	else:
		value = age_in_minutes // (60 * 24)
		precision = numberWord125(value, 'день', 'дня', 'дней')

	return "{0} {1} назад".format(value, precision)	