def invert_vert(list):
    N = int(len(list) ** 0.5)
    slices = [list[(i * N):(i * N + N)] for i in range(N)]
    for i in range(N):
        slices[i] = slices[i][::-1]
    slicesum = []
    for i in range(N):
        slicesum = slicesum + slices[i]
    for i in range(len(list)):
        list[i] = slicesum[i]


def rotate(list):
    N = int(len(list) ** 0.5)
    mule = [0 for i in range(len(list))]
    for i in range(N):
        for j in range(N):
            mule[i * N + j] = list[j * N + N -1 - i]
    for i in range(len(list)):
        list[i] = mule[i]
