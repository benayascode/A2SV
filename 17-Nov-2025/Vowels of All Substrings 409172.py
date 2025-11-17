# Problem: Vowels of All Substrings - https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:
        vow = "aeiou"
        c = 0
        for i in range(len(word)):
            if word[i] in vow:
                c += (i+1)*(len(word)-i)
        return c