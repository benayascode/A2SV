# Problem: Decode XORed Permutation - https://leetcode.com/problems/decode-xored-permutation/description/?envType=problem-list-v2&envId=bit-manipulation

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        x = 0
        for i in (encoded[::-2]):
            x ^= i
        for i in range(len(encoded)+2):
            x ^= i
        out = [x]
        for i in range(len(encoded)):
            out.append(out[i] ^ encoded[i])
        return out