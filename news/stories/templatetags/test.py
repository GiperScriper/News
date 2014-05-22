# -*- coding:utf-8 -*-

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


minutes = numberWord125(7, 'минута', 'минуты', 'минут')
hours = numberWord125(7, 'час', 'часа', 'часов')
days = numberWord125(7, 'день', 'дня', 'дней')
print minutes, hours, days
