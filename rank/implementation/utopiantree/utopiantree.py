t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    height = 1
    for num in range(n):
        if num == 1:
            height += 1
        elif num % 2 == 0:
            height *= 2
        else:
            height += 1
    print(height)


for _ in range(input()):
    n=input()
    print(pow(2,(n+1)/2+1)-1-(n%2))

# explanation added to info
def numbers():
    n = 4
    return ~(~1<<(n>>1))<<(n&1)

print(numbers())