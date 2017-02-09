time = input().strip().split(':')


def converter():
    ampm = time[2][-2:]
    if ampm == 'AM':
        if time[0] == '12':
            time[0] = '00'
        else:
            pass
    else:
        if time[0] != '12':
            time[0] = str(int(time[0]) + 12)
    time[2] = time[2][:2]
    return ':'.join(time)


print(converter())
