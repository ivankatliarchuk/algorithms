"""
TASK
The member states of the UN are planning to send 2 people to the Moon. But there is a problem. In line with their
principles of global unity, they want to pair astronauts of 2 different countries.
There are N trained astronauts numbered from 0 to N-1. But those in charge of the mission did not receive information about the
citizenship of each astronaut. The only information they have is that some particular pairs of astronauts belong to the same county.

You task is to compute in how many ways they can pick a pair of astronauts belonging to different countries. Assume that you are provided
enough pairs to let you identity the groups of astronauts even though you might not know their country directly. For instance , if 1,2,3
are astronauts from the same country; it is sufficient to mention that (1,2) and (2,3) are pairs of astronauts from the same country
withuot providing information about a third pair (1,2)
INPUT
The first line contains two integers, N and I, separated by a single space. I lines fillow. Each line contains 2 integers separated
by a single space A and B such that.
0 <= A, B <= N - 1
Where A and B are astronauts from the same country.
CONSTANTS
1 <= N <= 10^5
1 <= I <= 10^4
OUTPUT
An integer that denotes the number of permissible ways to choose a pair of astronauts.
SAMPLE INPUT
4 2
0 1
2 3
SAMPLE OUTPUT
4
EXPLANATION
Persons numbered 0 and 1 belong to same country, and those numbered 2 and 3 belong to same country. So the UN can choose one person
out of 0&1 and another person out of 2&3. So the number of ways of choosing a pair of astronauts is 4.
"""


# print("{0} {1}".format(N,I))

# find astronauts with no groups
# keeps extra table with astronaut-country
# find missing astronaut

def readCountries():
    N, I = list(map(int, input().split()))
    countries = {}
    astronauts = {}
    for i in range(I):
        A, B = list(map(int, input().split()))
        if A in astronauts:
            countryA = astronauts.get(A)
            astronautsA = countries.get(countryA)
            # add to astronauts
            if B in astronauts and astronauts.get(B) != countryA:
                countryB = astronauts.get(B)
                astronautsB = countries.pop(countryB)
                # move everyone to same country
                for a in astronautsB:
                    astronauts[a] = countryA
                    astronautsA.add(a)
            else:
                astronautsA.add(B)
                astronauts[B] = countryA

        elif B in astronauts:
            countryB = astronauts.get(B)
            astronautsB = countries.get(countryB)
            # add to astronauts
            if A in astronauts and A not in countryB:
                countryA = astronauts.get(A)
                astronautsA = countries.pop(countryA)
                # and reset country
                # move everyone to same country
                for a in astronautsA:
                    astronauts[a] = countryB
                    astronautsB.add(a)
            else:
                astronautsB.add(A)
                astronauts[A] = countryB
        else:
            astronauts[A] = i
            astronauts[B] = i
            countries[i] = {A, B}
    return (addMissingAstronauts(countries, astronauts, N), astronauts)


# find missin astronauts, as extra sets
def addMissingAstronauts(countries, astronauts, N):
    numbers = astronauts.keys()
    value = N - len(numbers)
    return (countries, value)

def countPosibilites():
    ((data, hidden), astronauts) = readCountries()
    combitaions = 0
    while len(data) > 0:
        (K, V) = data.popitem()
        local = 0
        localLength = len(V)
        for rem in V:
            astronauts.pop(rem)
        currentLength = len(astronauts) + hidden
        local += localLength * currentLength
        combitaions += local
    if hidden > 0:
        combitaions += (hidden - 1) / 2 * hidden
    return int(combitaions)

print(countPosibilites())
