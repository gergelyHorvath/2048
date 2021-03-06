import heur
import move
import copy
from main import possib_dir


def gen_poss_tabs(table):
    """
    In 2048 you either get a 2 or a 4 each move.
    This function creates a dictionary that contains all possible
    game states based on this rule, and their probability.
    """
    freeloc = []
    for i, j in enumerate(table):
        if j == 0:
            freeloc.append(i)
    utility = 0
    worktable = {}
    for i in freeloc:
        weight = 1 / len(freeloc) * 0.9
        worktable['2_{0}'.format(i)] = [copy.copy(table), weight]
        worktable['2_{0}'.format(i)][0][i] = 2

        weight = 1 / len(freeloc) * 0.1
        worktable['4_{0}'.format(i)] = [copy.copy(table), weight]
        worktable['4_{0}'.format(i)][0][i] = 4
    return worktable


def opt_move(table, depth=1):
    """
    The main decision making function of the AI.
    Evaluates moves based on possible game states 'depth'
    moves in the future.
    """
    directions = possib_dir(table)
    if len(directions) == 0:
        return [[], 10 ** 6]
    for i in directions:
        tables = copy.copy(gen_poss_tabs(directions[i]))
        directions[i] = 0
        for j in tables:
            if depth == 2:
                directions[i] += heur.heur(tables[j][0]) * tables[j][1]
            else:
                directions[i] += opt_move(tables[j][0], depth + 1)[1] * tables[j][1]
    greatchoice = min(directions, key=directions.get)
    return [greatchoice, directions[greatchoice]]
