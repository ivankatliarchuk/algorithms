numbers = list(map(int, input().split()))

numbers.sort()
print("{} {}".format(sum(numbers[:-1]), sum(numbers[1:])))
