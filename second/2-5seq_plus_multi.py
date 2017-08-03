#!/usr/bin/env python2  
# encoding: utf-8  

""" 
@version: v1.0 
@author: whyc
@license: Apache Licence  
@contact: 8720whyc@gmail.com
@site:  
@software: PyCharm 
@file: 2-5seq_plus_multi.py 
@time: 17-8-3 下午1:08
@description :
    test t序列使用 + 和 * 的应用
"""


def func():
    """
    + 和 * 都遵循这个规律， 不修改原有的操作对象， 而是构建一个全新的
    序列。
    如果在 a * n 这个语句中， 序列 a 里的元素是对其他可变
    对象的引用的话， 你就需要格外注意了， 因为这个式子的结果可能
    会出乎意料。 比如， 你想用 my_list = [[]] * 3 来初始化一个
    由列表组成的列表， 但是你得到的列表里包含的 3 个元素其实是 3
    个引用， 而且这 3 个引用指向的都是同一个列表。 这可能不是你想
    要的效果
    :return:
    """
    li = [1, 2, 3]
    print("5*'abc': ",5*'abc')
    print("test * 符号的引用 li * 5: li =[1,2,3] ", li * 5)

    #3X3 的列表推导 ，其中应用了 * 来表达
    board =[['_']*3 for i in range(3)] #➊
    print("board: ",board)
    board[2][1]="wwwwwd"  # ➋
    print("赋值给 board[2][1]:%s"%board)

    """
        ➊ 建立一个包含 3 个列表的列表， 被包含的 3 个列表各自有 3 个元
        素。 打印出这个嵌套列表。
        ➋ 把第 1 行第 2 列的元素标记为 X， 再打印出这个列表。
        示例 2-13 展示了另一个方法， 这个方法看上去是个诱人的捷径， 但实
        际上它是错的。
    """
    # 不使用列表推导式
    weird_board=[['_']*3]*3
    print("wired_board: ",weird_board)
    # 赋值一个元素值
    weird_board[1][1]='00o'
    print("赋值后的序列：",weird_board)


class Main():
    def __init__(self):
        pass
    func()


if __name__ == "__main__":
    Main()