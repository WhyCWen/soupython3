#!/usr/bin/env python2  
# encoding: utf-8  
"""
-------------------------------------------------
    @version        : v1.0 
    @File Name      : 2-7list_sort_sorted.py  
    @Author         : whyc
    @date           : 17-8-3 下午9:07
    @license        : 
    @contact        : 8720whyc@gmail.com
    @site           : https://github.com/WhyCWen 
    @software       : PyCharm 
    @file           : 2-7list_sort_sorted.py 
-------------------------------------------------
    @Description    : 
            list.sort 方法会就地排序列表， 也就是说不会把原列表复制一份。 这
        也是这个方法的返回值是 None 的原因， 提醒你本方法不会新建一个列
        表。 在这种情况下返回 None 其实是 Python 的一个惯例： 如果一个函数
        或者方法对对象进行的是就地改动， 那它就应该返回 None， 好让调用
        者知道传入的参数发生了变动， 而且并未产生新的对象。 例
        如， random.shuffle 函数也遵守了这个惯例。

            与 list.sort 相反的是内置函数 sorted， 它会新建一个列表作为返回
        值。 这个方法可以接受任何形式的可迭代对象作为参数， 甚至包括不可
        变序列或生成器（ 见第 14 章） 。 而不管 sorted 接受的是怎样的参
        数， 它最后都会返回一个列表。

        不管是 list.sort 方法还是 sorted 函数， 都有两个可选的关键字参
        数。
        reverse
            如果被设定为 True， 被排序的序列里的元素会以降序输出（ 也就
        是说把最大值当作最小值来排序） 。 这个参数的默认值是 False。
        key
            一个只有一个参数的函数， 这个函数会被用在序列里的每一个元素
        上， 所产生的结果将是排序算法依赖的对比关键字。 比如说， 在对一些
        字符串排序时， 可以用 key=str.lower 来实现忽略大小写的排序， 或
        者是用 key=len 进行基于字符串长度的排序。 这个参数的默认值是恒
        等函数（ identity function） ， 也就是默认用元素自己的值来排序。
-------------------------------------------------
    Modifictions    : Change Activity  @Times
    @Description    : 17-8-3 下午9:07
                    :
-------------------------------------------------

"""
__author__ = 'whyc'


def func():
    fruits = ['grape', 'raspberry', 'apple', 'banana'] #❶
    print("fruits sored: ",sorted(fruits))  # ❷
    print("reverse sorted:" ,sorted(fruits,reverse=True)) # ❸
    print("ken=len sorted: ",sorted(fruits,key=len)) #❹
    print("ken=len ,reverse = True sorted: ",sorted(fruits,key=len,reverse=True)) #❺
    #----------------------------------
    #使用 sort 排序
    print(fruits)   #  ❻

    fs = fruits.sort()
    print("sort return None:",fs) #❼
    print("sort : ",fruits)   #❽
    """
        ❶ 新建了一个按照字母排序的字符串列表。
        ❷ 原列表并没有变化。
        ❸ 按照字母降序排序。
        ❹ 新建一个按照长度排序的字符串列表。 因为这个排序算法是稳定
        的， grape 和 apple 的长度都是 5， 它们的相对位置跟在原来的列表里是
        一样的。
        ❺ 按照长度降序排序的结果。 结果并不是上面那个结果的完全翻转，
        7
        7
        因为用到的排序算法是稳定的， 也就是说在长度一样时， grape 和 apple
        的相对位置不会改变。
        ❻ 直到这一步， 原列表 fruits 都没有任何变化。
        ❼ 对原列表就地排序， 返回值 None 会被控制台忽略。
        ❽ 此时 fruits 本身被排序。
        已排序的序列可以用来进行快速搜索， 而标准库的 bisect 模块给我们
        提供了二分查找算法。 下一节会详细讲这个函数， 顺便还会看看
        bisect.insort 如何让已排序的序列保持有序。
    """
#把要运行的发放放在这里面 式逻辑运行
def run():
    func()


class Main():
    def __init__(self):
        pass


if __name__ == "__main__":
    run()