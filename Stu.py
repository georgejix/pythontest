from LogUtil import *


class Stu:
    """stu class"""
    TAG = 'Stu'
    stuCount = 0

    def __init__(self, name, age):
        log(Stu.TAG, 'self=', self)
        log(Stu.TAG, 'self.__class__=', self.__class__)
        self.name = name
        self.age = age
        Stu.stuCount += 1
        return

    def print_info(self):
        log(Stu.TAG, '__dict__=', Stu.__dict__)
        log(Stu.TAG, '__doc__=', Stu.__doc__)
        log(Stu.TAG, '__name__=', Stu.__name__)
        log(Stu.TAG, '__module__=', Stu.__module__)
        log(Stu.TAG, '__bases__=', Stu.__bases__)
        log(Stu.TAG, '', f'name={self.name},age={self.age}')
        return

    def __del__(self):
        log(Stu.TAG, id(self), 'Stu.del')
        return
