def shifty_sum(N, k):
    # non-formuliac solution
    # start with N, add rest one-by-one
    t = N
    for i in range(1, k+1):
        t += N*10**i
    return t

N = int(input())
k = int(input())
print(shifty_sum(N, k))