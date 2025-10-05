# Problem: Prime Palindrome - https://leetcode.com/problems/prime-palindrome/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def primePalindrome(self, n: int) -> int:
        def palin(s):
            return str(s) == str(s)[::-1]
        
        def prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    return False
            return True

        while True:
            if palin(n) and prime(n):
                return n
            n += 1
            if 10 ** 8 > n > 10 ** 7:
                n = 10 ** 8