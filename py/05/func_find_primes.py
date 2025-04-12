prime_list = []
sub_list = []
def find_primes(a,b):
    for n in range(a, b+1):
        if n<=1:
            sub_list.append(n)
        else:
            for i in range(2, n):
                if n % i == 0:
                    sub_list.append(n)

    for n in range(a, b+1):
        if not n in sub_list:
            prime_list.append(n)

    print(prime_list)


find_primes(1,11)