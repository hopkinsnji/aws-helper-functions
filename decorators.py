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

def aws_clean_fail(func):
    '''
    A decorator to cleanly exit on a failed call to AWS.
    catch a `botocore.exceptions.ClientError` raised from an action.
    This sort of error is raised if you are targeting a region that
    isn't set up.

    https://github.com/fugue/credstash/blob/b6d56359247440cc3fab8813b901f2118f464d46/credstash.py#L253

    '''
    def func_wrapper(*args, **kwargs):
        # from botocore.exceptions import ClientError

        try:
            return func(*args, **kwargs)
        except botocore.exceptions.ClientError as e:
            print(str(e), file=sys.stderr)
            logger.exception(e)
        except Exception as e:
            print(str(e), file=sys.stderr)
            logger.exception(e)
        sys.exit(1)
    return func_wrapper