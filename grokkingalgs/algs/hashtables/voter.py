voted = {}
voted['pedro'] = True
voted['sasha'] = False

def check_voter(name):
    if voted.get(name):
        print('Kick them out')
    else:
        voted[name] = True
        print('Let them vote!')

print(voted)
check_voter('sasha')
check_voter('gonzales')
check_voter('sasha')