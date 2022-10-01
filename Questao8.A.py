from random import randint
import time

N = 20000

def factorial(n):
    factorial = n
    for i in range(n - 1, 1, -1):
        factorial = factorial * i
    return (factorial)

#captura o tempo inicial
initial_time = float(time.time())

list_a = []
for i in range(N):
    list_a.append(randint(1, 15))

list_b = []
for i in list_a:
    list_b.append(factorial(i))

final_time = float(time.time())

print('Tempo total sequencial:', final_time - initial_time)