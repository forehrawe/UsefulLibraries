from numba import jit

@jit(nopython=True)
def main(n):
    total = 0
    for i in range(n):
        total += i
    return total

print(main(1000000))