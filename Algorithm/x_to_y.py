"""
对于一个数字x，给出两个变换规则：

    1）若x为偶数，那么可以变成x+1或者2*x；

    2）若x为奇数时，则只可以变换为2*x问题。

因此，对于任意的x,y。问x经过若干轮变换后，是否有可能变成y？
"""


def check_x_to_y(x, y):
    if x > y:
        return False
    elif x == y:
        return True
    else:
        if x % 2:
            return check_x_to_y(x=2*x, y=y)
        else:
            return check_x_to_y(x=x+1, y=y) or check_x_to_y(x=2*x, y=y)


if __name__ == '__main__':
    print(check_x_to_y(3, 16))
