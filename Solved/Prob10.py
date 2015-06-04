def prime_sieve(max):
    """Create a list containing all prime numbers equal to or less than max."""
    primes = range(max+1) # all numbers 0 to max
    primes[1] = 0 # 1 is not prime
    for number in primes: # iterate through all numbers
        if number: # if not 0 (i.e. prime)
            for multiple in range(2, (max // number) + 1):
                primes[number * multiple] = 0 # set multiples to zero
    return sum(primes)

print prime_sieve(input())
