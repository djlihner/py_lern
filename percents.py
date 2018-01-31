def percents(x, y):
    """Какой процент X от числа Y"""
    one_percent = x / 100
    result = y / one_percent
    return result


def print_percents(x, y):
    """Вывод на экран результата печати"""
    print(str(y) + " is " + str(percents(x, y)) + " % of " + str(x))


percents(200, 50)
