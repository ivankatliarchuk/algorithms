def analytics(text):
    count = 0
    while text:
        test = text[:3]
        # print("{} {} {} {}".format(test[:1], test[1], test[2], test))
        if test[0] != 'S':
            count += 1
        if test[1] != 'O':
            count += 1
        if test[2] != 'S':
            count += 1
        text = text[3:]
    return count


if __name__ == '__main__':
    S = input().strip()
    print(analytics(S))


# SOSOOSOSOSOSOSSOSOSOSOSOSOS

def alternative():
    S = input()
    assert len(S) % 3 == 0 and len(S) <= 99
    n = len(S) / 3
    exp = "SOS" * n  # Expected string
    ans = 0
    for i in range(len(S)):
         if exp[i] != S[i]:
             ans = ans + 1
    print(ans)

def alternativeS():
    print(len([1 for x,y in zip(input(),'SOS'*33) if x!=y]))
