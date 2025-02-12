# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        team = skill[0] + skill[-1]
        out = skill[0] * skill[-1]

        l ,r = 1 , len(skill)-2
        while l < r:
            if skill[l] + skill[r] != team:
                return -1
            out += (skill[l]*skill[r])
            l += 1
            r -= 1
        return out

