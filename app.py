
def romeu_julieta(value:int):
    if value % 3 == 0 and value % 5 == 0:
        return 'romeu e julieta'
    if value % 3 == 0:
        return 'queijo'
    if value % 5 == 0:
        return 'goiabada'