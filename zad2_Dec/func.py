def check_file_wrapper(func):
    def inner(*args, **kwargs):
        path = ''
        if len(args) > 0:
            path = args[0]
        elif kwargs.get('source', ''):
            path = kwargs.get('source')
        import os
        if path and os.path.exists(path):
            print('File exists')
        elif path:
            print('Path do not exist - file will be created')
            from pathlib import Path
            Path(path).touch()
        else:
            print('No argument given')
            import sys
            sys.exit(1)
        return func(*args, **kwargs)

    return inner


@check_file_wrapper
def writing_file(source: str):
    with open(source, 'r') as fd:
        fd.read()


def catch_io_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IOError as exe:
            print(f'IOError catched, more info {exe.args}')
        return None

    return inner


def catch_io_error_with_library(func):
    from functools import wraps

    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IOError as exe:
            print(f'IOError catched, more info {exe.args}')
        return None

    return inner


@catch_io_error_with_library
def read_no_existing_file():
    source = 'No existing file'
    with open(source, 'r') as fd:
        fd.read()


@catch_io_error
def throw_exception_file():
    raise IOError('test error')


def main():
    # writing_file(source='./test')
    throw_exception_file()
    read_no_existing_file()


main()
