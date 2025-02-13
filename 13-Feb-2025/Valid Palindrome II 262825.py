# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        p1=0
        p2=len(s)-1

        while p1 <= p2:
            if s[p1]!=s[p2]:
                if p2-p1 == 1:
                    return True
                p11 = p1
                p22 = p2
                if s[p1] == s[p2-1]:
                    p2 -= 1
                    while p1 <= p2:
                        if s[p1] != s[p2]:
                            break
                        p1 += 1
                        p2 -= 1
                    else:
                        return True
                p1 = p11
                p2 = p22
                if s[p1+1] == s[p2]:
                    p1 += 1
                    while p1 <= p2:
                        if s[p1] != s[p2]:
                            return False
                        p1 += 1
                        p2 -= 1
                else:
                    return False
                
            p1+=1
            p2-=1
        return True
        