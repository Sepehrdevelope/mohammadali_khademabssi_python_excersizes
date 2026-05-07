def is_prime(n):
    if n < 2 :
        return False
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True

for j in range(1,500):
    if is_prime(j) == True:
        print(j)
