#encoding=utf-8
import logging
import time
def print_calling(fn):
    def wrapper(*args1, ** args2):
        s = "calling function %s"%(fn.__name__)
        logging.info(s)
        start = time.time()
        ret = fn(*args1, **args2)
        end = time.time()
#         s = "%s. time used = %f seconds"%(s, (end - start))
        s = "function [%s] has been called, taking %f seconds"%(fn.__name__, (end - start))
        logging.debug(s)
        return ret
    return wrapper


def print_test(fn):
    def wrapper(*args1, ** args2):
        s = "running test: %s..."%(fn.__name__)
        logging.info(s)
        ret = fn(*args1, **args2)
        s = "running test: %s...succeed"%(fn.__name__)
        logging.debug(s)
        return ret
    return wrapper
    
def print_calling_in_short(fn):
    def wrapper(*args1, ** args2):
        start = time.time()
        ret = fn(*args1, **args2)
        end = time.time()
        s = "function [%s] has been called, taking %f seconds"%(fn.__name__, (end - start))
        logging.debug(s)
        return ret
    return wrapper

import collections
counter = collections.defaultdict(int)
def print_calling_in_short_for_tf(fn):
    import tensorflow as tf
    import util
    def wrapper(*args1, ** args2):
        start = time.time()
        thread_name = util.thread.get_current_thread_name()
        ret = fn(*args1, **args2)
        end = time.time()
        counter[fn.__name__] = counter[fn.__name__] + (end - start)
        all_time = sum([counter[name] for name in counter]) * 1.0
        for name in counter:
            tf.logging.info('\t %s: %f, %f seconds'%(name, counter[name] / all_time, counter[name]))
        s = "Thread [%s]:function [%s] has been called, taking %f seconds"%(thread_name, fn.__name__, (end - start))
        tf.logging.info(s)
        return ret
    return wrapper


