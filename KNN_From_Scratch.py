def ED(co_ordinate, test_point, k):
    dist = []
    for group in co_ordinate:
        for feature in co_ordinate[group]:
            # calculate the euclidean distance
            euclidean_distance = ((feature[0] - test_point[0]) ** 2 + (feature[1] - test_point[1]) ** 2) ** 0.5

            dist.append((euclidean_distance, group))

    # Sorting

    distance = sorted(dist)[:k]

    f1 = 0
    f2 = 0

    for i in distance:
        if i[1] == 0:
            f1 += 1
        elif i[1] == 1:
            f2 += 1

    if f1 > f2:
        return 0
    else:
        return 1


def knn():
    co_ordinate = {0: [(1, 1), (1, 2), (2, 1), (1.8, 1.9), (1, 2), (1.5, 3.5), (1, 5), (2.5, 1), (2, 2.5), (2, 1.5)],
                   1: [(5, 2.5), (4.5, 5), (5, 6), (5.5, 4), (6, 3), (6, 5), (7, 4), (6.5, 4)]}

    # testing point p(x,y)
    test_point = (3,8)  # Try different Points to check in which class it belongs 

    # Number of neighbours
    k = 3

    print("The Class of unknown point",test_point, "lies in Class",(ED(co_ordinate, test_point, k))) 
knn()
