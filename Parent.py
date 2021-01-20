from LogUtil import log


class Parent:
    TAG = 'Parent'
    parentAttr = 100
    __parentAttr = 200  #私有变量

    def __init__(self):
        log(Parent.TAG, '', 'parent 构造函数')
        return

    def parent_method(self):
        log(Parent.TAG, '', '调用父类方法')
        return

    def set_attr(self, attr):
        log(Parent.TAG, 'set_attr=', attr)
        Parent.parentAttr = attr
        return

    def get_attr(self):
        log(Parent.TAG, 'parentAttr=', Parent.parentAttr)
        return