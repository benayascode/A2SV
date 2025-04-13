# Problem: Count Vowel Substrings of a String - https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        out = 0
        for i in range(len(word)):             
            check = set()
            for j in range(i,len(word)):
                if word[j] in 'aeiou':
                    check.add(word[j])
                    if len(check)>=5:
                        out += 1
                else:
                    break                
        return out  