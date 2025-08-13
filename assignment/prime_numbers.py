
N = int(input("Enter the value of N: "))
num = 2  

print(f"Prime numbers up to {N} are:")

while num <= N:
    is_prime = True
    divisor = 2

    while divisor * divisor <= num:
        if num % divisor == 0:
            is_prime = False
            break
        divisor += 1

    if is_prime:
        print(num, end=" ")

    num += 1  

print("\nDone! All primes up to", N, "are displayed.")
