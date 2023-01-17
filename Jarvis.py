def Jarvis(points: list):
    # wyszukanie skrajnego lewego
    p_idx = 0
    first_from_left = (10000,100000)
    for idx,point in enumerate(points):
        if point[0] < first_from_left[0]:
            first_from_left = point
        elif point[0] == first_from_left[0]:
            if point[1] < first_from_left[1]:
                first_from_left = point
                p_idx = idx

    #główna pętla tworząca otoczkę
    sheath = []
    p = first_from_left

    while True:
        sheath.append(p)

        q = points[(p_idx + 1)%len(points)]

        for index,r in enumerate(points):
            if r != p and r != q:
                orient = orientation(p,q,r)
                if orient == 'clockwise':
                    q = r

        p = q
        p_idx = points.index(p)
        if p == first_from_left:
            break
    return sheath

def Jarvis_v2(points: list):
    # wyszukanie skrajnego lewego
    p_idx = 0
    first_from_left = (10000,100000)
    for idx,point in enumerate(points):
        if point[0] < first_from_left[0]:
            first_from_left = point
        elif point[0] == first_from_left[0]:
            if point[1] < first_from_left[1]:
                first_from_left = point
                p_idx = idx

    #główna pętla tworząca otoczkę
    sheath = []
    p = first_from_left

    while True:
        sheath.append(p)

        q = points[(p_idx + 1)%len(points)]

        for index,r in enumerate(points):
            if r != p and r != q:
                orient = orientation(p,q,r)
                if orient == 'linear':
                    if distance(p, q) < distance(p, r):
                        q = r
                elif orient == 'clockwise':
                    q = r
        p = q
        p_idx = points.index(p)
        if p == first_from_left:
            break
    return sheath

def orientation(p, q, r):
    length = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if length < 0:
        return 'counterclockwise'

    elif length > 0:
        return 'clockwise'

    elif length == 0:
        return 'linear'

def distance(p, q):
    return ((p[0] - q[0]) * (p[0] - q[0]) + (p[1] - q[1]) * (p[1] - q[1]))

def main():
    points_1 = [(0, 3), (0, 0), (0, 1), (3, 0), (3, 3)]
    points_2 = [(0, 3), (0, 1), (0, 0), (3, 0), (3, 3)]

    sheath_1 = Jarvis(points_1)
    sheath_2 = Jarvis(points_2)
    print(sheath_1)
    print(sheath_2)

    sheath_1_v2 = Jarvis_v2(points_1)
    sheath_2_v2 = Jarvis_v2(points_2)
    print(sheath_1_v2)
    print(sheath_2_v2)
    points_3 = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]

    sheath_3 = Jarvis(points_3)
    sheath_3_v2 = Jarvis_v2(points_3)
    print('Pierwsza wersja algorytmu :', sheath_3, '\n')
    print('Druga wersja algorytmu :', sheath_3_v2)
main()