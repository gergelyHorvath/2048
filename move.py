import invert, copy


def move(list):
    N = int(len(list) ** 0.5)
    dummylist = copy.copy(list)
    for i in range(N):
        for j in range(N):
            for doittwice in [0, 1]:
                counter = 0
                while list[i * N + j] == "":
                    if counter == N - 1:
                        break
                    for k in range(j, N-1):
                        list[i * N + k] = list[i * N + k + 1]
                    list[i * N + N - 1] = ""
                    counter += 1
                if (j > 0) and (list[i * N + j] != "") and (doittwice == 0):
                    if list[i * N + j] == list[i * N + j - 1]:
                        list[i * N + j - 1] = str(int(list[i * N + j]) + int(list[i * N + j - 1]))
                        list[i * N + j] = ""
    a_valid_move = 1
    if list == dummylist:
        a_valid_move = 0
    return a_valid_move


def move_right(list):
    invert.invert_vert(list)
    valid = move(list)
    invert.invert_vert(list)
    return valid


def move_up(list):
    invert.rotate(list)
    valid = move(list)
    for thrice in range(3):
        invert.rotate(list)
    return valid


def move_down(list):
    invert.rotate(list)
    invert.invert_vert(list)
    valid = move(list)
    invert.invert_vert(list)
    for thrice in range(3):
        invert.rotate(list)
    return valid

