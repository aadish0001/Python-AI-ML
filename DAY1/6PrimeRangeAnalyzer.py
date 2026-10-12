A = int(input())
B = int(input())
prime_count = 0

for n in range(A, B + 1):
    if n < 2:
        continue

    is_prime = True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        prime_count += 1

print(prime_count)