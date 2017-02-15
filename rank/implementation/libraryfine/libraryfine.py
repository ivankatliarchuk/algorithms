def analytics(first, second):
    year = Ya - Ye
    month = Ma - Me
    days = Da - De
    if year > 0:
        fine = 10000
    elif month > 0 and year >= 0:
        fine = 500 * month
    elif days > 0 and month >= 0 and year >= 0:
        fine = 15 * days
    else:
        fine = 0
    return fine


if __name__ == '__main__':
    Da,Ma,Ya = (map(int, input().split()))
    De,Me,Ye = (map(int, input().split()))
    print(analytics((De,Me,Ye), (Da,Ma,Ya)))
