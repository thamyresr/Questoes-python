import threading, time
from random import randint

def fatorial(n):
    fatorial = n
    for i in range(n - 1, 1, -1):
        fatorial = fatorial * i
    return(fatorial)

def calcular_fatorial(lista, inicio, fim):
    for i in range(inicio, fim):
        list_b.append(fatorial(lista[i]))

tempo_inicio = float(time.time())

N = 20000
list_b = []

#preenchendo a lista
lista_a = []
for i in range(N):
    lista_a.append(randint(1, 10))

Nthreads = 4

lista_threads = []
for i in range(Nthreads):
    inicio = i * int(N / Nthreads) #inicia o intervalo da lista
    fim = (i + 1) * int(N / Nthreads) #fim do intervalo da lista
    thread = threading.Thread(target=calcular_fatorial, args=(lista_a, inicio, fim))
    thread.start() #inicia a thread
    lista_threads.append(thread) #guarda a thread

for thread in lista_threads:
    thread.join() #espera as threads terminarem

tempo_final = float(time.time())

print('Tempo total em paralelo:', tempo_final - tempo_inicio)