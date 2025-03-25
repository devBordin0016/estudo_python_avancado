def function_teste():
    print("Ola Mundo Magnifico!")

    yield

    print("Vou te contar uma historia")

    yield

    print("De como funcionar o coroutine")

    yield

def function_teste2():
    print('Funciona assim')

    yield

    print('Executa um proceso')

    yield

    print('Ai o yield basicamente esta realizando uma pausa')

    yield

    print('Assim ele da continuidade aos demais comandos')


try:
    a = function_teste()
    b = function_teste2()

    next(a)
    next(a)
    next(a)
    next(b)
    next(b)
    next(b)
    next(b)
except StopIteration as e:
    pass
