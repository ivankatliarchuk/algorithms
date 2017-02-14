def analytics(N, M, S):
    if S > N:
        S = N % S
    if M > N:
        M = M % N
    lastIndex = S + (M - 1)

    if lastIndex <= N:
        index = lastIndex
    else:
        overflow = lastIndex - N
        index = overflow
    print(index)


if __name__ == '__main__':
    T = int(input().strip())
    for test in range(T):
        N, M, S = list(map(int, input().split()))
        analytics(N, M, S)
