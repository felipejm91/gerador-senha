def continua():
    op = input("\n\nGerar outra senha? (S/N) ").upper()
    if op == 'Y':
        op = 1
    elif op == 'N':
        op = 0

    return op
