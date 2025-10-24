#Pattern Used: Two Pointers / Math Reverse Pattern
#Why this pattern?: We need to reverse the digits of the number and compare it with the 
# original number.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x!=0 and x%10==0):
            return False
        revHalf = 0
        while x > revHalf:
            revHalf = revHalf * 10 + x % 10
            x = x // 10
        
        return x == revHalf or x == revHalf //  10
    
#calls to the function can be made as follows:
sol = Solution()
print(sol.isPalindrome(121))  # True
