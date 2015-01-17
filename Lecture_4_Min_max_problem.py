lo = 4
hi = 10
x = 12

def clip(lo, x, hi):
    x = max (lo, x)
    x = min (x, hi)
    return x
