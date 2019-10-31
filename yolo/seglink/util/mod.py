#coding=utf-8

import logging

def add_to_path(path):
    '''
    add path to sys.path.
    '''
    import sys;
    sys.path.insert(0, path);

def add_ancester_dir_to_path(fp, p):
    '''
    add ancester directory to sys.path.
    fp: usually __file__
    p : the relative path to be added.
    '''
    import util
    parent_path = util.io.get_dir(fp)
    path = util.io.join_path(parent_path, p)
    add_to_path(path)

def is_main(mod_name):
    return mod_name == '__main__'
    
def import_by_name(mod_name):
    __import__(mod_name)
    return get_mod_by_name(mod_name)

def try_import_by_name(mod_name, error_path):
    try:
        import_by_name(mod_name)
    except ImportError:
        logging.info('adding %s to sys.path'%(error_path))
        add_to_path(error_path)        
        import_by_name(mod_name)
    
    return get_mod_by_name(mod_name)
    
def get_mod_by_name(mod_name):
    import sys
    return sys.modules[mod_name]
    

