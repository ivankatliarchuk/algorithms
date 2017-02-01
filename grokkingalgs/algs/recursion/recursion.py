def countDown(i):
    print(i)
    if i <= 0: # base case
        return
    else: # recursive case
        countDown(i - 1)


# countDown(5)
def fact(i):
    if i == 1:
        return 1
    else:
        return i * fact(i - 1)

print(fact(5))
