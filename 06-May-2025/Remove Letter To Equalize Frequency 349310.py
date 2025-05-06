# Problem: Remove Letter To Equalize Frequency - https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        mydict = {}
        for i in word:
            if i in mydict:
                mydict[i] += 1
            else:
                mydict[i] = 1
        for char in list(mydict.keys()):
            mydict[char] -= 1
            if mydict[char] == 0:
                del mydict[char]
            if len(set(mydict.values())) == 1:
                return True
            if char in mydict:
                mydict[char] += 1
            else:
                mydict[char] = 1
        return False