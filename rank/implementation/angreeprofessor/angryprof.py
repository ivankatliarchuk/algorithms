def analytics(students, threshold):
    arrived = list(filter(lambda n: n <= 0, students))
    if len(arrived) >= threshold:
        result = "NO"
    else:
        result = "YES"
    print(result)



if __name__ == '__main__':
    T = int(input().strip())
    for test in range(T):
        N, K = list(map(int, input().split()))
        students = list(map(int, input().split()))
        analytics(students, K)

'''
a1 = filter(lambda x:x <= 0, map(int, raw_input().split()))
    print ["YES", "NO"][len(a1) >= k]
'''
