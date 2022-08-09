"""
Nth prime program - given int N, returns Nth prime
"""

def is_prime(number):
    for ind in range(2, number//2+1):
        if number % ind == 0:
            return False
    else:
        return True


def prime(number):
    prime_list = [2,3,5,7,11,13,17,19]
    if number == 0:
        raise ValueError("there is no zeroth prime")
    if len(prime_list) >= number:
        return prime_list[number-1]
    for ind in range(19, number**4, 2):
        if is_prime(ind):
            prime_list.append(ind)
        if len(prime_list) >= number+1:
            return prime_list[number]
