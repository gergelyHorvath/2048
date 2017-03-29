def drawagrid(list):
    N = int(len(list) ** 0.5)
    space = " "
    thisrow = "┌"
    for i in range(N):
        thisrow += (7 * "─" + "┬")
    print(thisrow[:-1] + "┐")
    for i in range(N):
        for j in range(1):
            print(("│" + space * 7) * N + "│")
        thisline = ""
        for j in range(N):
            nbr = str(list[j + i * N])
            dist = int((7 - len(nbr)) // 2)
            thisline += "│" + " " * dist + nbr + " " * (7 - len(nbr) - dist)
        print(thisline + "│")
        for j in range(1):
            print(("│" + " " * 7) * N + "│")
        if i < N - 1:
            print("├" + ("─" * 7 + "┼") * (N - 1) + "─" * 7 + "┤")
    thisrow = "└"
    for i in range(N):
        thisrow += (7 * "─" + "┴")
    print(thisrow[:-1] + "┘")




