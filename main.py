import random, copy, draw, move, invert, highscores
import recur


def strtable(table):
    nums = []
    for i in table:
        nums.append("" if i == 0 else str(i))
    return nums


def randomplace(list):
    freeloc = []
    for i, j in enumerate(list):
        if j == 0:
            freeloc.append(i)
    randidx = random.choice(freeloc)
    if random.randint(1, 10) > 9:
        list[randidx] = 4
    else:
        list[randidx] = 2


def possib_dir(table):
    directions = {}
    table_up = copy.copy(table)
    if move.move_up(table_up) == 1:
        directions["w"] = table_up
    table_left = copy.copy(table)
    if move.move(table_left) == 1:
        directions["a"] = table_left
    table_down = copy.copy(table)
    if move.move_down(table_down) == 1:
        directions["s"] = table_down
    table_right = copy.copy(table)
    if move.move_right(table_right) == 1:
        directions["d"] = table_right
    return directions


def main():
    usr = input("Enter your name:")
    if usr == "":
        usr = "NamelessPlayer"
    try:
        size = input("Enter the prefered game boaed size 2-10:")
        size = int(size)
        if size not in range(2, 11):
            size = 4
    except ValueError:
        size = 4
    moves = 0
    table = [0 for i in range(size ** 2)]
    randomplace(table)
    while True:
        print("\n" * 100)
        for i in range(1):
            randomplace(table)
        draw.drawagrid(strtable(table))
        directions = possib_dir(table)

        if len(directions) == 0:
            print("Game Over!")
            highscores.hsc(strtable(table), usr, moves, size)
            quit()

        if usr == 'AI':
            dirinput = recur.opt_move(table)[0]

        else:
            dirinput = input("Enter a possible direction ({0}):".format(", ".join(list(directions.keys()))))
            while dirinput not in directions:
                dirinput = input()
        if dirinput == "w":
            table = copy.copy(directions['w'])
        elif dirinput == "s":
            table = copy.copy(directions['s'])
        elif dirinput == "a":
            table = copy.copy(directions['a'])
        elif dirinput == "d":
            table = copy.copy(directions['d'])
        moves += 1


if __name__ == '__main__':
    main()




