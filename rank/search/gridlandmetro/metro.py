tracks = {}


def analytics(cellCount):
    counter = 0
    for key, val in tracks.items():
        if type(val[0]) is int:
            S, E = val
            occupied = (E - S) + 1
            # print("{} {} diff {}".format(S, E, (E - S) + 1))
            counter += occupied
        else:
            for dv in val:
                occupied = (dv[1] - dv[0]) + 1
                counter += occupied
    return cellCount - counter


if __name__ == '__main__':
    Row, Col, NTracks = list(map(int, input().strip().split(' ')))
    for track in range(NTracks):
        R, C1, C2 = list(map(int, input().strip().split(' ')))
        if tracks.get(R) is None:
            tracks[R] = [C1, C2]
        else:
            oc = tracks.get(R)
            # first check if intersect
            if (C1 <= oc[1] and C2 >= oc[1]):
                if C1 < oc[0]:
                    tracks[R][0] = C1
                if C2 > oc[1]:
                    tracks[R][1] = C2
            elif C1 > oc[1] or C2 < oc[0]:
                extra = [C1, C2]
                tracks[R] = [oc, extra]

    # print(tracks)
    print(analytics(Row * Col))
