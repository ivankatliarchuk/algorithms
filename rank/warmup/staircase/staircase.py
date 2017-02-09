N = int(input().strip())

for num in range(N):
    empty = " " * (N - num - 1)
    hash = "#" * (num + 1)
    print("{0}{1}".format(empty, hash))