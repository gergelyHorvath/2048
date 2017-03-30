

def hsc(list, usr, moves, size):
    """
    Handles the game when Game Over conditions are met.
    Exports, imports high scores.
    """
    highestelement = 0
    for i in list:
        if int(i) > highestelement:
            highestelement = int(i)
    print("Your Score:{0}".format(highestelement))
    print("It took you {0} moves".format(moves))
    try:
        with open("Highscores{0}.txt".format(size), "r") as f:
            scores = f.readlines()
        scoreslistified = []
        for i in scores:
            scoreslistified.append(i.split())
        ialreadyexchangedone = False
        for i in scoreslistified:
            if int(highestelement) > int(i[1]):
                if not ialreadyexchangedone:
                    scoreslistified.insert(scoreslistified.index(i), [usr, highestelement, moves])
                    ialreadyexchangedone = True
            elif int(highestelement) == int(i[1]):
                if moves <= int(i[2]):
                    if not ialreadyexchangedone:
                        scoreslistified.insert(scoreslistified.index(i), [usr, highestelement, moves])
                        ialreadyexchangedone = True
        if not ialreadyexchangedone:
            scoreslistified.append([usr, highestelement, moves])
        if len(scoreslistified) > 10:
            del scoreslistified[10]
        scoresretextified = []
        for i in scoreslistified:
            for j in range(3):
                i[j] = str(i[j])
            scoresretextified.append(" ".join(i) + "\n")
        with open("Highscores{0}.txt".format(size), "w") as f:
            f.writelines(scoresretextified)
    except FileNotFoundError:
        with open("Highscores{0}.txt".format(size), "w") as f:
            scores = str(usr) + " " + str(highestelement) + " " + str(moves)
            f.write(scores)
            scoresretextified = []
            scoresretextified.append(scores)
    print("\nHighScores(Username, Higest block, Moves): ")
    print("\n")
    for i in range(1, 1 + len(scoresretextified)):
        print("{0}.    ".format(i) + scoresretextified[i-1])