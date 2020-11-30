## Ex2.
def vn(N):
    L = [0] * (N+1)
    for n in range(0, N):
        L[n+1] = (2*L[n]+3)/(L[n]+4)
    return L
