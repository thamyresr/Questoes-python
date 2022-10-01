import multiprocessing, time, random


def fatorial(n):
    fat = n
    for i in range(n - 1, 1, -1):
        fat = fat * i
    return (fat)


def calcular_fatoria_lista(lista, q2):
    lista_b = []
    for i in lista:
        fat = fatorial(i)
        lista_b.append(fat)
    q2.put(lista_b)


if __name__ == "__main__":
    N = 10000

    t_inicio = float(time.time())

    lista_a = []
    for i in range(N):
        lista_a.append(random.randint(1, 10))

    lista_b = []
    inicio = 0
    contador = 1
    NProc = 4
    q_saida = multiprocessing.Queue()
    lista_proc = []

    for i in range(NProc):
        fim = int((N // NProc) * contador)
        p = multiprocessing.Process(target=calcular_fatoria_lista, args=(lista_a[inicio:fim], q_saida))
        p.start()
        lista_proc.append(p)
        inicio = fim
        contador += 1

    while q_saida.empty is False:
        for process in lista_proc:
            process.join()

    for i in range(0, NProc):
        for i in q_saida.get():
            lista_b.append(i)

    t_fim = float(time.time())
    print('Tempo total em segundos:', t_fim - t_inicio)

    input('finalize o programa!!!!')
