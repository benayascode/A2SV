# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre = [arr[0]]
        for i in range(1,len(arr)):
            x = pre[i-1] ^ arr[i]
            pre.append(x)

        print(pre)
        out = [0] * len(queries)
        i = 0
        for a,b in queries:
            out[i] = pre[b] ^ pre[a-1] if a > 0 else pre[b]
            i += 1
        return out
