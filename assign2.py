import logging
from logging import getLogger

log = getLogger(__name__)

class DebuggerTest(object):
    def __init__(self, func):
        self.func = func

    def __call__ (self, *args, **kwargs):
        print 'my function name is: %s' % self.func.func_name
        _ret = self.func(*args, **kwargs)

        print 'my function name also is: %s' % self.func.func_name
        return _ret

@DebuggerTest
def avgPrice(arg1, arg2):
    print 'Avg price is 1st purch price %r being averaged by 2nd purch price %r: %r' % (arg1, arg2, (arg1 + arg2)/2)
    return ((arg1 + arg2)/2)


@DebuggerTest
def Total_traded(arg1, arg2):
    print 'Total traded is price %r times shares %r: %r is total dollar amount traded' % (arg1, arg2, arg1 * arg2)
    return arg1 * arg2

logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this too')

