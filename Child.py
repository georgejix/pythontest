from LogUtil import log
from Parent import *


class Child(Parent):
    '''
    单下划线、双下划线、头尾双下划线说明：

    __foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。

    _foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *

    __foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。
    '''
    TAG = 'Child'
    childAttr = 100
    __childAttr = 200  # 私有变量

    def __init__(self):
        super().__init__()
        log(Parent.TAG, '', 'Child 构造函数')
        return

    def child_method(self):
        log(Child.TAG, '', '调用子类方法')
        return
