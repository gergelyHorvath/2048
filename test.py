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
        for i in freeloc:
            worktable = copy.copy(table)
            worktable[i] = '2'
            weight = 1 / len(freeloc) *0.9
            utility += heur.heur(worktable) * weight

            worktable[i] = '4'
            weight = 1 / len(freeloc) * 0.1
            utility += heur.heur(worktable) * weight
    return utility


def opt_move(table):
    directions = possib_dir(table)
    for i in directions:
        directions[i] = gen_poss_tabs(directions[i])
    return min(directions, key=directions.get)




    

