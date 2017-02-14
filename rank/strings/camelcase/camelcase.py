
def countWords(words):
    count = 1
    for word in words:
        if word.isupper():
            count += 1
    return count


if __name__ == '__main__':
    S = input().strip()
    print(countWords(S))