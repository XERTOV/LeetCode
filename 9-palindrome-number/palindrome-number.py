class Solution:
    def isPalindrome(self, x: int) -> bool:
        new_x = str(x)
        if new_x == new_x[::-1]:
            return True
        return False
        