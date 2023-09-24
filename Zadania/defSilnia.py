def fact(nr):
    if nr == 0:
        return 1
    else:
        return nr * fact(nr-1)
