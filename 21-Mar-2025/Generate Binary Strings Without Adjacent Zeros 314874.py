# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []
        x = [""]*n

        def rec(index):
            if index == n:
                # for k in range(n-1):
                #     if int(x[k]) + int(x[k+1]) == 0:
                #         break
                # else:
                res.append("".join(x))
                return

            for num in ["0", "1"]:
                if num == "0" and index > 0 and x[index-1] == "0":
                    continue
                x[index] = num
                rec(index + 1)
                x[index] = ""

        rec(0)
        return res

