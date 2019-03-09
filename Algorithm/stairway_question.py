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
from functools import lru_cache
# 增加functools.lru_cache装饰器，主要用来做缓存，能把相对耗时的函数结果进行保存
# 避免传入相同参数进行重复计算，缓存不会无限增长，不用的缓存会被释放


@lru_cache(10**8)
def method_count(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return method_count(n-1) + method_count(n-2)


if __name__ == '__main__':
    test_n = 99
    print(method_count(test_n))
