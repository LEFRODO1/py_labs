def falling(n, k):
    """Рассчитать убывающий факториал от n глубины k.
    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
    "*** YOUR CODE HERE ***"
    result = 1
    while k > 0:
        result = result * n
        n, k = n - 1, k - 1
    return result 


def sum_digits(y):
    """Сложить все цифры числа y..
    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """
    "*** YOUR CODE HERE ***"
    sum = 0
    while y > 0:
        sum, y = sum + y % 10, y // 10
    return sum


def double_eights(n):
    """Возвращает True если в n есть две цифры 8 подряд.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    state = False
    while n > 0:
        if n % 10 == 8:
            if state:
                state = True
        else:
            state = False
        n = n // 10
    return False