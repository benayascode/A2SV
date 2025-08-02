# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def rec(curr, ind, temp, cnt):
            nonlocal out
            if cnt > 4:
                return
            if cnt == 4 and ind == len(curr):
                out.append(temp[:-1])
            
            for i in range(1,4):
                if ind+i > len(curr):
                    break
                s = curr[ind:ind+i]
                if (s[0] == "0" and len(s) > 1)  or (i == 3 and int(s) > 255):
                    continue
                rec(curr,ind+i, temp+s+".", cnt+1)
        out = []
        rec(s, 0, "", 0)
        return out
