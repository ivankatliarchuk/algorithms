"""
TASK
Alise and Bob each created one problem. A reviewer rates the two challanges, awarding points on a scale from 1 to 100 for
three categories: problem clarity, originality and difficulty.
We define the rating for Alice's challange to be the triplet A = {ao, a1, a2} and the rating for Bob's challenge
to be the triplet B = (b0, b1, b2).
Your task is to find their comparison scores by comparing a0 with b0, a1 with b1, a2 with b2
if ai > bi, then Alice is awarded 1 point
if ai < bi, then Bob is awarded 1 point
if a1 = b1, then neither person receives a point
Given A and B, can you compare the two challenges and print their respective comparison points?
INPUT
The first line contains 3 space-separated integers, a0, a1, a2 describing the respective values in tripletA
The second line contains 3 space separated integers, b0, b1 and b2 describing the respective values in triplet B
CONSTANTS
1 <= a <= 100
1 <= b <= 100
OUTPUT
Print two space-separated integers denoting the respective comparison scores earned by Alice and Bob.
SAMPLE INPUT
5 6 7
3 6 10
SAMPLE OUTPUT
1 1
"""

a0, a1, a2 = input().strip().split(' ')
first = (a0, a1, a2) = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
second = (b0, b1, b2) = [int(b0), int(b1), int(b2)]

score = [0, 0]

for index, x in enumerate(first):
    # print("{0} and {1} corresponds {2}".format(index, x, second[index]))
    if x > second[index]:
        score[0] += 1
    elif x < second[index]:
        score[1] += 1

print("{0} {1}".format(score[0], score[1]))

# A = (a0>b0) + (a1>b1) + (a2>b2)
"""
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

print(sum(a > b for a, b in zip(A, B)), sum(a < b for a, b in zip(A, B)))
"""


