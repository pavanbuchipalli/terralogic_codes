def recu(n):
    if len(n) <= 1:
        return n
    else:
        return recu(n[1:]) + n[0]


recu("pavan")