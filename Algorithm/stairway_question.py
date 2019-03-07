"""
有n个台阶，如果一次只能上一个或者两个台阶，总共有多少种上法？
定义函数F(n)
n 为台阶数
n = 1: F(1) = 1
n = 2: F(2) = 2
n = 3: F(3) = 3
n = 4: F(4) = 5
n = 5: F(5) = 8

可以看出规律F(n) = F(n-1) + F(n-2)

"""


def method_count(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return method_count(n-1) + method_count(n-2)


if __name__ == '__main__':
    n = 36
    print(method_count(n))
