import multiprocessing

def cpu_count():
    return multiprocessing.cpu_count()

def get_pool(processes):
    pool = multiprocessing.Pool(processes = processes)
    return pool

def wait_for_pool(pool):
    pool.close()
    pool.join()  

def set_proc_name(name):
    import setproctitle
    setproctitle.setproctitle(name)