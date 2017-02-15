alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']
width = 1


def maxHeight(table, txt):
    result = -1
    for char in txt:
        val = table[char]
        if val > result:
            result = val
    return result


def analytics(table, txt):
    height = maxHeight(table, txt)
    return len(txt) * width * height


if __name__ == '__main__':
    # list of all character
    chars = list(map(chr, range(97, 123)))
    print(chars)
    heights = list(map(int, input().split()))
    txt = input().strip()
    # map alphabet values to their heights
    dictionary = dict(zip(alphabet, heights))
    print(analytics(dictionary, txt))

    '''
    size = [int(i) for i in input().split()]
word = [size[ord(c)-ord('a')] for c in input()]
print(max(word)*len(word))
    '''
