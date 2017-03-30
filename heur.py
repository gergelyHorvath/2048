"""
The heuristics of the AI.
The AI prefers tables with as few monotonity changes as possible
and a board with low deviation.
"""

import invert
import copy
import math


def heuristicsrows(table):
    length = int(len(table) ** 0.5)
    scorerows = []
    scorecol = []
    for rows in range(length):
        monotonity = [0]
        scorerows.append(0)
        for cols in range(1, length):
            diff = table[rows * length + cols] - table[rows * length + cols - 1]
            if diff > 0:
                monotonity.append(1)
            elif diff < 0:
                monotonity.append(-1)
            else:
                monotonity.append(0)
            if monotonity[cols] == -1 * monotonity[cols - 1]:
                scorerows[rows] += abs(diff)
    return sum(scorerows)


def heuristicscols(table):
    temptable = copy.copy(table)
    invert.rotate(temptable)
    return heuristicsrows(temptable)


def heurhomog(table):
    avg = sum(table) / len(table)
    std_dev = math.sqrt(sum([(i - avg) ** 2 for i in table]) / len(table))
    return std_dev


def heur(table):
    multi = 1
    if max(table) > 512:
        multi = 0
    return (heuristicsrows(table) + heuristicscols(table)) * 10 + multi * heurhomog(table)
