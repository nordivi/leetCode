# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
#
# You can either start from the step with index 0, or the step with index 1.
#
# Return the minimum cost to reach the top of the floor.

from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    if not cost:
        return 0
    l = len(cost)
    df = [0] * l
    df[0] = cost[0]
    if l > 1:
        df[1] = cost[1]
    for i in range(2, l):
        df[i] = cost[i] + min(df[i - 1], df[i - 2])
    return min(df[-1], df[-2])


minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1])