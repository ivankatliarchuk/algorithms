import sys

# read a line of input and convert it into a list
nums = list(map(int, input().split()))
data = sys.stdin.readlines()[0].split()


a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]


for line in sys.stdin:
    print(line)
