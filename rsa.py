import sys
import random
import numpy as np

def count_digits(number):
    return int(np.log10(number))+1

def load_primes(primes_file):
    # load first 10k primes from file
    with open(primes_file, 'r') as fp:
        return list(map(int, fp.readlines()))

def choose_p_and_q(primes, n_digits, E):
    p = q = 0
    p_digits = 0
    q_digits = 0

    while p_digits != 5:
        p = random.choice(primes)
        p_digits = count_digits(p)

    while q != p and q_digits != 5:
        q = random.choice(primes)
        q_digits = count_digits(q)

    while np.gcd((p-1)*(q-1), E) != 1:
        choose_p_and_q(primes, n_digits)

    return p, q

def extended_gcd(a, b):
    x,y, u,v = 0, 1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b

    return x

def keygen(primes):

    e = 65537
    p, q = choose_p_and_q(primes, 5, e)
    N = p * q
    d = extended_gcd(e, (p-1)*(q-1))

    print(f"p={p} q={q}")
    print(f"N={N}")
    print(f"e={e} d={d}")
    print(f"\nPublic key = ({N}, {e})")
    print(f"Private key = ({N}, {d})")

    return N, e, d

def encrypt(m, public_key):
    m = [ord(c) for c in m]
    print(m)

def decrypt(m, private_key):
    m = pow(c, d) % mod n

if __name__ == '__main__':
    primes = load_primes("primes.txt")
    N, e, d = keygen(primes)
    public_key  = {'N' : N, 'e' : e}
    private_key = {'N' : N, 'd' : d} 

   

