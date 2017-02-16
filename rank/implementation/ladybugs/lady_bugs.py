def analytics(bugs):
    data = {}
    underscore = 0
    prevBug = ''
    flag = True
    for bug in bugs:
        #  check whether there is one by one
        if prevBug == '_' and data.get(bug) is None:
            prevBug = bug
        elif prevBug == '' or bug == '_' or prevBug == bug or data.get(bug) is None:
            prevBug = bug
        else:
            flag = False
        # assemble
        if bug == '_':
            underscore += 1
        elif data.get(bug) is None:
            data[bug] = 1
        else:
            data[bug] += 1

    if flag and len(data) > 0 and min(data.values()) > 1:
        return 'YES'
    elif len(data) == 0 and underscore > 0:
        return 'YES'
    elif min(data.values()) == 1:
        return 'NO'
    elif underscore == 0:
        return 'NO'
    return "YES"

    # if underscore == 0:
    #     return 'NO'
    # values = data.values()
    # if values is None :
    #     return 'NO'
    # elif len(values) > 0 and min(values) == 1:
    #     return 'NO'
    # else:
    #     return 'YES'


if __name__ == '__main__':
    G = int(input().strip())
    for game in range(G):
        int(input().strip())
        bugs = list(map(str, input().strip()))
        print(analytics(bugs))
