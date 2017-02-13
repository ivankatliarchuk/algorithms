
s,t = map(int, input().split())
a,b = map(int, input().split())
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apples = [int(apple_temp) for apple_temp in input().strip().split(' ')]
oranges = [int(orange_temp) for orange_temp in input().strip().split(' ')]

app_house = []

for apple in apples:
    location = apple + a
    if location >= s and location <= t:
        app_house.append(apple)

orange_house = []
for orange in  oranges:
    if orange < 0:
        location = orange + b
        if location >= s and location <= t:
            orange_house.append(orange)

print("{} \n{}".format(len(app_house), len(orange_house)))

