# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note: The solution set must not contain duplicate combinations.

def combination_sum_ii(candidates, target):
    candidates.sort()

    res = []

    def backtrack(cur, i, target):
        if target == 0:
            res.append(cur.copy())
        if target <= 0:
            return
        prev = -1
        for i in range(len(candidates)):
            if candidates[i] == prev:
                continue
            res.append(candidates[i])
            backtrack(cur, i+1, target - candidates[i])
            cur.pop()
            prev = candidates
    backtrack([], 0, target)
    return res