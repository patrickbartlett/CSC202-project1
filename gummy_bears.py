
def bears(n):
    """A True return value means that it is possible to win
    the bear game by starting with n bears. A False return value means
    that it is not possible to win the bear game by starting with n
    bears."""

    if n == 42:
        return True
    if n < 42:
        return False
    if n % 2 == 0:
        if bears(int(n/2)):
            return True
    if (n % 3 == 0 or n % 4 == 0) and mult_last_two(n):
        if bears(n - mult_last_two(n)):
            return True
    if n % 5 == 0:
        if bears(n - 42):
            return True
    return False


def mult_last_two(num):
    """multiples last two digits of number"""

    string_num = str(num)

    num1 = int(string_num[-1:])
    string_num = string_num[:-1]
    num2 = int(string_num[-1:])

    if num1 == 0 or num2 == 0:
        return False

    return num1 * num2



