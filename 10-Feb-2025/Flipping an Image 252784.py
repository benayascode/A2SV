# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        out = []
        for i in image:
            s = i[::-1]
            for j in range(len(s)):
                if s[j] == 0:
                    s[j] += 1
                else:
                    s[j] -= 1
            out.append(s)
        return out