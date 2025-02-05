# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        out = []
        s = []
        i = 0
        while  num:
            out.append((num%10)*(10**i))
            i += 1
            num //= 10
        out.reverse()
        print(out)
        for i in out:
            if i >= 1000:
                x = (i//1000)
                s.append(x*"M")
            elif i == 900:
                s.append("CM")
            elif i >=  500:
                x = (i-500)//100
                s.append("D"+(x*"C"))
            elif i == 400:
                s.append("CD")
            elif i >= 100:
                x = i//100
                s.append((x*"C"))
            elif i == 90:
                s.append("XC")
            elif i >= 50:
                x = (i-50)//10
                s.append("L"+(x*"X"))
            elif i == 40:
                s.append("XL")
            elif i >= 10:
                x = i//10
                s.append((x*"X"))
            elif i == 9:
                s.append("IX")
            elif i >= 5:
                x = (i-5)
                s.append("V"+(x*"I"))
            elif i == 4:
                s.append("IV")
            else:
                s.append(i*"I")

            

        return ("".join(s))

             
    
