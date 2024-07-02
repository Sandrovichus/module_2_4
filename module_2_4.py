numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []
for i in numbers:
    if i == 1:  # исключаем 1, так как это не простое и не составное число
        continue
    is_prime = True  # по умолчанию число пусть будет простым
    for j in range(2, i):  # делим элемент на числа от 2 до ближайшего меньшего, пока не найдем делитель
        if i % j == 0:  # если делится без остатка - число не простое, проверку завершаем
            is_prime = False
            break
    if is_prime:  # в зависмимости от признака добавляем элемент в соответствующий список
        primes.append(i)
    else:
        not_primes.append(i)

print('Primes:', primes)
print('Not primes:', not_primes)
