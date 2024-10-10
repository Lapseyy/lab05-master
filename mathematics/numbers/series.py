def sum(list=None):
    return __builtins__['sum'](list)


def average(list = None):
    # ave = __builtins__['sum'](list) / len(list)
    # return ave
    return sum(list) / len(list)
