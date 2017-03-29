import invert
import copy
import math


def numtable(table):
    nums = []
    for i in table:
        nums.append(0 if i == '' else int(i))
    return nums


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
    nums = numtable(table)
    return (heuristicsrows(nums) + heuristicscols(nums)) * 10 + heurhomog(nums)


# a_table = [2, 2, 4, 4, 8, 4, 8, 2, 2, 16, 16, 32, 128, 2, 256, 1024]

# print(heuristicsrows(a_table))
# print(heuristicscols(a_table))
# print(heurhomog(a_table))


       




