# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        out = []
        for i in range(len(img)):
            s = []
            for j in range(len(img[0])):
                c = 1
                tot = img[i][j]
                if j + 1 < len(img[0]):
                    tot += img[i][j+1]
                    c += 1
                if j - 1 > -1:
                    tot += img[i][j-1]
                    c += 1
                if i+1 < len(img):
                    tot += img[i+1][j]
                    c += 1
                if i-1 > -1:
                    tot += img[i-1][j]
                    c += 1
                if i-1 > -1 and j-1 > -1:
                    tot += img[i-1][j-1]
                    c += 1
                if i-1 > -1 and j+1 < len(img[0]):
                    tot += img[i-1][j+1]
                    c += 1
                if i+1 < len(img) and j-1 > -1:
                    tot += img[i+1][j-1]
                    c += 1
                if i+1 < len(img) and j+1 < len(img[0]):
                    tot += img[i+1][j+1]
                    c += 1
                s.append(tot//c)
            out.append(s)
        return out

                
