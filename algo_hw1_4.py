### Problem 4: Finds the fraction with O(1) including cyclical

# Finds the start of the cycle
def go_to_cycle(num, den):
    i = num
    j = num
    while True:
        i = (10 * i) % den
        j = 10 * (10 * j % den) % den
        if i == j:
            return i

# Finds the length of the loop which iterates
def loop_len(num, den):
    rem = num
    k = 0
    while True:
        rem = 10 * rem % den
        k += 1
        if rem == num:
            return k

def find_start(num, den, length):
    i = num
    j = num
    for l in range(length):
        j = 10 * j % den
    k = 0
    while True:
        if i == j:
            return k
        i = 10 * i % den
        j = 10 * j % den
        k += 1

def string_to_fraction_o1(num, den):
    # num //= den
    print(num // den, end='.')
    num = num % den

    num_new = go_to_cycle(num, den)
    k = loop_len(num_new, den)
    l_start = find_start(num, den, k)
    for i in range(l_start):
        print(10 * num // den, end='')
        num = 10 * num % den
    print('(', end='')
    for i in range(k):
        print(10 * num // den, end='')
        num = 10 * num % den
    print(')')

string_to_fraction_o1(3, 5)
