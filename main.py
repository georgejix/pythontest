from LogUtil import *
from Stu import *
from Child import Child


def test_stu():
    zs = Stu('zhangSan', 18)
    zs.print_info()
    ls = Stu('liSi', 19)
    log(TAG, 'Stu.stuCount=', Stu.stuCount)
    log(TAG, 'hasattr age=', hasattr(zs, 'age'))
    log(TAG, 'hasattr sex=', hasattr(zs, 'sex'))
    log(TAG, 'getattr age=', getattr(zs, 'age'))
    log(TAG, 'zs id=', id(zs))
    log(TAG, 'ls id=', id(ls))
    del zs
    #    del ls
    return


def test_child():
    c = Child()
    c.child_method()
    c.parent_method()
    c.set_attr(25)
    c.get_attr()
    log(TAG, 'Child.parentAttr', Child.childAttr)
#    log(TAG, 'Child.__parentAttr', Child.__childAttr)
    #访问私有变量方法
    log(TAG, 'Child.parentAttr', c._Child__childAttr)
    return


if __name__ == '__main__':
    TAG = 'main'
    #test_stu()
    test_child()




