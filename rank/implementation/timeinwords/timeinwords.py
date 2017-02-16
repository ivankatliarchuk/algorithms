hours = {1: 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10: 'ten',
         11: 'eleven'}

minutes = {
    00: '{} o\' clock',
    1: 'one minute {} {}',
    2: 'two minutes {} {}',
    3: 'three minutes {} {}',
    4: 'four minutes {} {}',
    5: 'five minutes {} {}',
    6: 'six minute {} {}',
    7: 'seven minutes {} {}',
    8: 'eight minutes {} {}',
    9: 'nine minutes {} {}',
    10: 'ten minutes {} {}',
    11: 'eleven minutes {} {}',
    12: 'twelve minutes {} {}',
    13: 'thirteen minutes {} {}',
    14: 'fourteen minutes {} {}',
    15: 'quarter {} {}',
    16: 'sixteen minutes {} {}',
    17: 'seventeen minutes {} {}',
    18: 'eighteen minutes {} {}',
    19: 'nineteen minutes {} {}',
    20: 'twenty munutes {} {}',
    25: 'twenty five minutes {} {}',
    29: 'twenty nine minutes {} {}',
    30: 'half {} {}',
    40: 'twenty minutes {} {}',
    45: 'quarter {} {}',
}

def analytics(H, M):
    firstHalf = True
    if M > 30:
        M = 60 - M
        firstHalf = False
    minute = minutes.get(M)

    if firstHalf:
        hour = hours.get(H)
        val = 'past'
    else:
        hour = hours.get(H + 1)
        val = 'to'
    if M == 0:
        return minute.format(hour)
    else:
        return minute.format(val, hour)

if __name__ == '__main__':
    H = int(input().strip())
    M = int(input().strip())
    print(analytics(H, M))