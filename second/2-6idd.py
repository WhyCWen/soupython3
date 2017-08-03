#!/usr/bin/env python2  
# encoding: utf-8  
"""
-------------------------------------------------
   @version        : v1.0 
   @File Name      : 2-6idd   
   @Author         : whyc
   @date           : 17-8-3
   @license        : Apache Licence  
   @contact        : 8720whyc@gmail.com
   @site           :  
   @software       : PyCharm 
   @file           : 2-6idd.py 
-------------------------------------------------
   Change Activity :
             @time : 17-8-3 下午3:53   17-8-3:
-------------------------------------------------
   @Description    : 
   
   
-------------------------------------------------

"""
__author__ = 'whyc'

# ------------------------------------------------
"""
     我们已经认识了 += 的一般用法， 下面来看一个有意思的边界情况。 这
    个例子可以说是突出展示了“不可变性”对于元组来说到底意味着什么。
    一个关于+=的谜题
    读完下面的代码， 然后回答这个问题： 示例 2-14 中的两个表达式到底
    会产生什么结果？ 回答之前不要用控制台去运行这两个式子。
"""

def func():
    """
    实例 2-15 关于 += 的一个谜题

    :return:
    """
    t = (1,2,3,[30,40])
    try:
        t[3] += [50, 60]
    except Exception as e:
        print(e)
    print(t)
    #使用 t[3].extent([90,10o])
    t[3].extend([90,100])
    print(t)

    # 书中的结果
    """
        a. t 变成 (1, 2, [30, 40, 50, 60])。
        b. 因为 tuple 不支持对它的元素赋值， 所以会抛出 TypeError 异常。
        c. 以上两个都不是。
        d. a 和 b 都是对的。
        我刚看到这个问题的时候， 异常确定地选择了 b， 但其实答案是 d， 也
        就是说 a 和 b 都是对的！ 示例 2-15 是运行这段代码得到的结果， 用的
        Python 版本是 3.4， 但是在 2.7 中结果也一样。
        示例 2-15 没人料到的结果： t[2] 被改动了， 但是也有异常抛出
        >>> t = (1, 2, [30, 40])
        >>> t[2] += [50, 60]
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        TypeError: 'tuple' object does not support item assignment
        >>> t
        (1, 2, [30, 40, 50, 60])
    """
    # 本实例测试结果 符合A,b 选项，
    """
        t = (1, 2, 3, [30, 40])
        t[3] += [50, 60]
        Traceback (most recent call last):
          File "/home/whyc/softwares/anaconda3/lib/python3.6/site-packages/IPython/core/interactiveshell.py", line 2881, in run_code
            exec(code_obj, self.user_global_ns, self.user_ns)
          File "<ipython-input-4-ae24f7a9d68f>", line 2, in <module>
            t[3] += [50, 60]
        TypeError: 'tuple' object does not support item assignment
        t
        Out[5]: (1, 2, 3, [30, 40, 50, 60])

    """

    # 查看Python执行的字节码
    import dis
    print(dis.dis("s[a]+=b"))

    """ 
    生成的字节码 
    
  1           0 LOAD_NAME                0 (s)
              2 LOAD_NAME                1 (a)
              4 DUP_TOP_TWO
              6 BINARY_SUBSCR            #➊ 
              8 LOAD_NAME                2 (b)
             10 INPLACE_ADD              #➋ 
             12 ROT_THREE
             14 STORE_SUBSCR             #➌ 
             16 LOAD_CONST               0 (None)
             18 RETURN_VALUE
None

        ➊ 将 s[a] 的值存入 TOS（ Top Of Stack， 栈的顶端） 。
        ➋ 计算 TOS += b。 这一步能够完成， 是因为 TOS 指向的是一个可变对
        象（ 也就是示例 2-15 里的列表） 。
        ➌ s[a] = TOS 赋值。 这一步失败， 是因为 s 是不可变的元组（ 示例 2-15

        至此我得到了 3 个教训。
        不要把可变对象放在元组里面。
        增量赋值不是一个原子操作。 我们刚才也看到了， 它虽然抛出了异
        常， 但还是完成了操作。
        查看 Python 的字节码并不难， 而且它对我们了解代码背后的运行机
        制很有帮助
    """

#把要运行的发放放在这里面 式逻辑运行
def run():
    func()

class Main():
    def __init__(self):
        pass


if __name__ == "__main__":
    run()