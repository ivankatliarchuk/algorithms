from collections import Counter

def analytics(data, T):
    grouped = Counter(data)
    K,V = grouped.most_common(1).pop()
    print(T - V)

if __name__ == '__main__':
    T = int(input().strip())
    data = list(map(int, input().split()))
    analytics(data, T)
