from logging import getLogger

log = getLogger(__name__)

class DebuggerTest(object):
    def __init__(self, func):
        self.func = func

    def __call__ (self, *args, **kwargs):
        print 'i am the arguments before function execution %s' % self.func.func_name
        _ret = self.func(*args, **kwargs)

        print 'i am the arguments after function execution %s' % self.func.func_name
        return _ret

@DebuggerTest
def avgPrice(arg1, arg2):
    print '1st purch price %r being averaged by 2nd purch price %r: %r' % (arg1, arg2, (arg1 + arg2)/2)
    return ((arg1 + arg2)/2)


@DebuggerTest
def Total_traded(arg1, arg2):
    print 'price %r times shares %r: %r is total dollar amount traded' % (arg1, arg2, arg1 * arg2)
    return arg1 * arg2

