class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        fac = []
        for i in  range(1, n+1):
            if n%i == 0:
                fac.append(i)
        if k <= len(fac):
                return fac[k-1]
        else:
             return -1
                
