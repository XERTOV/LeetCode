class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        for i in s:
            stack.append(i)
            if (len(stack)>= 2 and ((stack[-2]=="["  and stack [-1] == "]"))):
             stack.pop()
             stack.pop()
        tot_swap = len(stack)//2
               
        return  (tot_swap+ 1)//2
        