def analytics(data):
    data.sort()
    amount = len(data)
    toRemove = 0
    decrementer = 0
    height = 0
    for num in data:
        if decrementer == num:
            toRemove += 1
            height += decrementer
        else:
            amount -= toRemove
            decrementer = num
            toRemove = 1
            print(amount)

if __name__ == '__main__':
    int(input().strip())
    numbers = list(map(int, input().split()))
    analytics(numbers)
