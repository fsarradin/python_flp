# fp.py -
#

def is_number(x):
    """
    a -> Bool
    """
    return isinstance(x, (int, float, complex))

def is_sequence(x):
    """
    a -> Bool
    """
    return isinstance(x, (list, tuple, range))

def is_empty(sequence):
    """
    [a] -> bool
    """
    return len(sequence) == 0

def head(sequence):
    """
    [a] -> a
    """
    return sequence[0]

def tail(sequence):
    """
    [a] -> [a]
    """
    return sequence[1:]

def __oper(f, unit, from_unit=True):
    """
    Num a => (((a, a) -> a), a, Bool) -> [a] -> a
    """
    def __op(sequence):
        result = unit
        if from_unit:
            for x in sequence:
                result = f(result, x)
        else:
            if not is_empty(sequence):
                result = sequence[0]
                for x in sequence[1:]:
                    result = f(result, x)
        return result

    return __op

def add(sequence):
    return __oper((lambda x, y: x + y), 0)(sequence)

def mul(sequence):
    return __oper((lambda x, y: x * y), 1)(sequence)

def sub(sequence):
    return __oper((lambda x, y: x - y), 0, from_unit=False)(sequence)

def div(sequence):
    return __oper((lambda x, y: x / y), 1, from_unit=False)(sequence)

def _and(sequence):
    return __oper((lambda x, y: x and y), True)(sequence)

def _or(sequence):
    return __oper((lambda x, y: x or y), False)(sequence)

def _not(sequence):
    """

    """
    if len(sequence) != 1:
        raise ValueError
    return not sequence[0]

def apply(f):
    """
    (a -> b) -> [a] -> [b]
    """
    def apply_on(sequence):
        return tuple(f(x) for x in sequence)
    return apply_on

def partbin(f, x):
        """
        (((a, b) -> c), a) -> b -> c
        """
        def partbin_on(y):
            return f([x, y])
        return partbin_on

def identity(x):
    """
    a -> a
    """
    return x

def cons(*f_seq):
    """
    [a -> b] -> a -> [b]
    """
    def cons_on(x):
        return tuple(f(x) for f in f_seq)
    return cons_on

def cst(x):
    """
    a -> b -> a
    """
    def cst_on(y):
        return x
    return cst_on

def foldLeft(f):
        """
        ((a, b) -> b) -> [a] -> b
        """
        def foldLeft_on(sequence):
            if len(sequence) == 1:
                return sequence[0]
            return f((sequence[0], foldLeft_on(sequence[1:])))
        return foldLeft_on

def do(*f_seq):
    """
    (a -> b)* -> a -> b
    """
    def do_on(x):
        result = x
        for f in f_seq:
            result = f(result)
        return result
    return do_on

def equal(sequence):
    """
    (a, b) -> Bool
    """
    if not is_sequence(sequence) or len(sequence) != 2:
        raise ValueError
    return sequence[0] == sequence[1]

def transpose(sequence):
    """
    [[a]] -> [[a]]
    """
    if is_empty(sequence):
        return sequence
    result = tuple([] for x in sequence[0])
    for i in range(len(sequence)):
        for j in range(len(sequence[i])):
            result[j].append(sequence[i][j])
    return result

def cond(p, t, e):
    """
    ((a -> Bool), (a -> b), (a -> b)) -> a -> b
    """
    def cond_on(x):
        if p(x):
            return t(x)
        return e(x)
    return cond_on

def compose(*f_seq):
    """
    (a -> b)* -> (c -> a) -> c -> b
    """
    def compose_with(*g_seq):
        if len(g_seq) > 1 or hasattr(g_seq[0], '__call__'):
            return compose(*(f_seq + g_seq))
        result = g_seq[0]
        for f in reversed(f_seq):
            result = f(result)
        return result
    return compose_with

def range_from(start):
    """
    Num a => a -> a -> [Int]
    """
    def _range(x):
        return range(start, x + 1)
    return _range

def get(x):
    """
    Int -> [a] -> a
    """
    def get_on(sequence):
        return sequence[x]
    return get_on

def filter(f):
    """
    (a -> Bool) -> [a] -> [a]
    """
    def filter_on(sequence):
        return tuple(v for v in sequence if f(v))
    return filter_on

def _eval(sequence):
    """
    ((a -> b), a) -> b
    """
    return sequence[0](sequence[1])

# End
