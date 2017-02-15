import math

friends = 3

def analytics(N):
    count = 0
    people = 5
    for num in range(N):
        likes = math.floor(people/2)
        # print("like the advert {} ".format(likes))
        # dislike = people - likes
        count += likes
        receivedAdvNextDay = math.floor(people/2) * 3
        people = receivedAdvNextDay
        # print("{0}               {0:b}".format(count))
    return count


if __name__ == '__main__':
    # print(bin(2))
    # print(bin(3))
    # print(bin(4))
    # print(bin(5))
    # print(bin(6))
    # print(bin(7))
    N = int(input().strip())
    print(analytics(N))
