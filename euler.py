# Problem 1 - sum of all multiples of 3 or 5 below 1000

def problem1(): 
    sum_multiples = sum(a for a in range(1000) if (a % 3 == 0 or a % 5 == 0))
    return str(sum_multiples)

print(problem1())

# Problem 2 - sum of all even Fibonacci numbers below 4 million

def problem2():
    sum = 0
    c = 1
    d = 2
    while c <= 4000000:
        if c % 2 == 0:
            sum += c
        c, d = d, c+d
    return str(sum)

print(problem2())

# Problem 3 - largest prime factor of the number 600851475143

n = 600851475143
e = 2

while e * e < n:
    while n % e == 0:
        n = n / e
    e = e + 1

print(int(n))
