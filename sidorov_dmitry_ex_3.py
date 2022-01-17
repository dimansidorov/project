def type_logger(func):
    def wrapper(*args):
        for i in args:
            print(f'{i}: {type(i)}')
        return func(*args)

    return wrapper


@type_logger
def calc_cube(*args):
    result = [el ** 3 for el in args]
    return result


a = calc_cube(5)
