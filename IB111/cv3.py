from __future__ import print_function

def mean(n):
    s = 0
    for i in range(1, n):
        s += i
    return float(s)/n
# print(mean(10))

def digit_sum(n):
    x = 0
    while(n>0):
        x += n % 10
        n = n / 10
    return x


def repeated_digit_sum(n):
    x=1
    while(x > 0):
        n = digit_sum(n)
        x = n / 10
    return n
# print(repeated_digit_sum(169))

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    print(f)
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True


def primes_less_than(limit):
    for i in range(limit):
        if is_prime(i) == True:
            print(i, end=' ')
# primes_less_than(20)

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

print(primes(20))


def dec_to_bin(x):
    return int(bin(x)[2:])
print(dec_to_bin(5))


def decimal_to_binary(n):
    while n > 0:
        x = n % 2
        n /= 2
        print(x)


decimal_to_binary(5)