import heur
import move
import copy
from main import possib_dir


def gen_poss_tabs(table):
    freeloc = []
    for i, j in enumerate(table):
        if j == "":
            freeloc.append(i)
    utility = 0
    worktable = {}
    for i in freeloc:
        weight = 1 / len(freeloc) * 0.9
        worktable['2_{0}'.format(i)] = [copy.copy(table), weight]
        worktable['2_{0}'.format(i)][0][i] = '2'

        weight = 1 / len(freeloc) * 0.1
        worktable['4_{0}'.format(i)] = [copy.copy(table), weight]
        worktable['4_{0}'.format(i)][0][i] = '4'
    return worktable


def opt_move(table):
    directions = possib_dir(table)
    for i in directions:
        tables = copy.copy(gen_poss_tabs(directions[i]))
        directions[i] = 0
        for j in tables:
            directions[i] += heur.heur(tables[j][0]) * tables[j][1]
    print(directions)
    print(min(directions, key=directions.get))
    return min(directions, key=directions.get)
