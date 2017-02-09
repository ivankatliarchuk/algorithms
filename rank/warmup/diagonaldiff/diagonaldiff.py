N = int(input().strip())

counter = 0
count = 0
for num in range(N):
    line = list(map(int, input().strip().split(' ')))
    length = len(line)
    count += line[counter] - line[length - counter - 1]
    # print("{} {}".format(line[counter], line[length - counter - 1]))
    counter += 1

print(abs(count))

