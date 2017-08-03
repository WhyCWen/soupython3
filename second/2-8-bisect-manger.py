#!/usr/bin/env python2  
# encoding: utf-8  
"""
-------------------------------------------------
    @version        : v1.0 
    @File Name      : 2-8-bisect-manger.py  
    @Author         : whyc
    @date           : 17-8-3 下午10:24
    @license        : 
    @contact        : 8720whyc@gmail.com
    @site           : https://github.com/WhyCWen 
    @software       : PyCharm 
    @file           : 2-8-bisect-manger.py 
-------------------------------------------------
    @Description    : 
            bisect 模块包含两个主要函数， bisect 和 insort， 两个函数都利用
        二分查找算法来在有序序列中查找或插入元素。
            bisect(haystack, needle) 在 haystack（ 干草垛） 里搜索
        needle（ 针） 的位置， 该位置满足的条件是， 把 needle 插入这个位置
        之后， haystack 还能保持升序。 也就是在说这个函数返回的位置前面
        的值， 都小于或等于 needle 的值。 其中 haystack 必须是一个有序的
        序列。 你可以先用 bisect(haystack, needle) 查找位置 index， 再
        用 haystack.insert(index, needle) 来插入新值。 但你也可用
        insort 来一步到位， 并且后者的速度更快一些。
-------------------------------------------------
    Modifictions    : Change Activity  @Times
    @Description    : 17-8-3 下午10:24
                    :
                    :
-------------------------------------------------

"""
__author__ = 'whyc'

import bisect
import sys

HAYSTACK = [1, 2, 3, 9, 6, 8, 2, 9, 10, 6, 8, 10, 25, 13, 24]
NEEDLES = [0, 1, 2, 5, 8, 10, 13, 24,25]
ROW_FMT = '{0:2d} @ {1:4}  {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK,needle) #➊
        offset = position * '  |'              #➋
        print(ROW_FMT.format(needle,position,offset)) #➌
def func():
    if sys.argv[-1] == 'left':#➍
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect
    print('DEMO:', bisect_fn.__name__) #➎
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)

"""
    ❶ 用特定的 bisect 函数来计算元素应该出现的位置。
    ❷利用该位置来算出需要几个分隔符号。
    ❸ 把元素和其应该出现的位置打印出来。
    ❹ 根据命令上最后一个参数来选用 bisect 函数。
    ❺ 把选定的函数在抬头打印出来。
"""
#把要运行的发放放在这里面 式逻辑运行
def run():
    func()


class Main():
    def __init__(self):
        pass


if __name__ == "__main__":
    run()