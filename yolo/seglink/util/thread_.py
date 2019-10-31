import threading
from threading import Thread

def get_current_thread():
    return threading.current_thread()

def get_current_thread_name():
    return get_current_thread().getName()
    
def is_alive(t):
    return t.is_alive()
    
def create_and_start(name, target, daemon = True):
    t = Thread(target= target)
    t.daemon = True
    t.setName(name)
    t.start()
    return t

