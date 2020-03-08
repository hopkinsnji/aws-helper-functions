def timer(func):
    ''' Decorate functions with this function get execution time.
    '''
    import time # If not imported at the top.
    def wrapper(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        t1 = time.time()
        print('Exexcution time:', t1-t0)
        return result
    return wrapper