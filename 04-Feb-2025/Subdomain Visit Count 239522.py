# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mydict = defaultdict(int)
        
        for dom in cpdomains:
            c, domain = dom.split(" ")
            c = int(c)
            
            sbd = domain.split(".")          
            for i in range(len(sbd)):
                j = ".".join(sbd[i:])
                mydict[j] += c

        result = [str(i) + " " + sub for sub, i in mydict.items()]
        
        return result