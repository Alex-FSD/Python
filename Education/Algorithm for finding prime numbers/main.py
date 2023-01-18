import time
from math import sqrt

n = 10000

##############
# 1 Алгоритм #
##############
print("1 Алгоритм")
start = time.time()
lst = []
k = 0
for i in range(2, n + 1):
    for j in range(2, i):
        if i % j == 0:
            k = k + 1
    if k == 0:
        lst.append(i)
    else:
        k = 0
end = time.time() - start
print(end)

##############
# 2 Алгоритм #
##############
print("2 Алгоритм")
start = time.time()
lst = []
for i in range(2, n + 1):
    for j in range(2, i):
        if i % j == 0:
            # если делитель найден, число не простое.
            break
    else:
        lst.append(i)
end = time.time() - start
print(end)

##############
# 3 Алгоритм #
##############
print("3 Алгоритм")
start = time.time()
lst = []
for i in range(2, n + 1):
    # пробегаем по списку (lst) простых чисел
    for j in lst:
        if i % j == 0:
            break
    else:
        lst.append(i)
end = time.time() - start
print(end)

##############
# 4 Алгоритм #
##############
print("4 Алгоритм")
start = time.time()
lst = []
for i in range(2, n + 1):
    for j in lst:
        if j > int((sqrt(i)) + 1):
            lst.append(i)
            break
        if (i % j == 0):
            break
    else:
        lst.append(i)
end = time.time() - start
print(end)

##############
# 5 Алгоритм #
##############
print("5 Алгоритм")
start = time.time()
lst = []
for i in range(2, n + 1):
    if (i > 10):
        if (i % 2 == 0) or (i % 10 == 5):
            continue
    for j in lst:
        if j > int((sqrt(i)) + 1):
            lst.append(i)
            break
        if (i % j == 0):
            break
    else:
        lst.append(i)
end = time.time() - start
print(end)

##############
# 6 Алгоритм #
##############
print("6 Алгоритм")
start = time.time()
lst = [2]
for i in range(3, n + 1, 2):
    if (i > 10) and (i % 10 == 5):
        continue
    for j in lst:
        if j > int((sqrt(i)) + 1):
            lst.append(i)
            break
        if (i % j == 0):
            break
    else:
        lst.append(i)
end = time.time() - start
print(end)

##############
# 7 Алгоритм #
##############
print("7 Алгоритм")
start = time.time()
lst = [2]
for i in range(3, n + 1, 2):
    if (i > 10) and (i % 10 == 5):
        continue
    for j in lst:
        if j * j - 1 > i:
            lst.append(i)
            break
        if (i % j == 0):
            break
    else:
        lst.append(i)
end = time.time() - start
print(end)

##############
# 8 Алгоритм ########
# Решето Эратосфена #
#####################
print("8 Алгоритм")
print("Решето Эратосфена")
start = time.time()
a = [n for n in range(n + 1)]
a[1] = 0
lst = []
i = 2
while i <= n:
    if a[i] != 0:
        lst.append(a[i])
        for j in range(i, n + 1, i):
            a[j] = 0
    i += 1
end = time.time() - start
print(end)
