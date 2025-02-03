# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = defaultdict()
        los = defaultdict()
        for i,j in matches:
            if i not in los:
                win[i] = 1
            else:
                if i in los and i in win:
                    del win[i]
            if j in los:
                los[j]+=1
            else:
                los[j] = 1
            if j in win:
                del win[j]
        w = [i for i in win]
        l = [i for i in los if los[i] == 1]
        return [sorted(w),sorted(l)]
