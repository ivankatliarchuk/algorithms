n,k,q = input().strip().split(' ')
n,K,q = [int(n),int(k),int(q)]

a = [int(a_temp) for a_temp in input().strip().split(' ')]

for num in range(K):
    a.insert(0, a.pop())

data = []
for a0 in range(q):
    m = int(input().strip())
    data.append(a[m])

for x in data:
    print(x)
