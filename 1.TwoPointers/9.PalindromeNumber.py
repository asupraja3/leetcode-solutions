#Pattern Used: Two Pointers / Math Reverse Pattern
#Why this pattern?: We need to reverse the digits of the number and compare it with the 
# original number.
# Time Complexity: O(log10(n)) where n is the input number. This is because we are processing
# each digit of the number once. Constants are ignored in Big O notation. so /2 is ignored.
# Space Complexity: O(1) as we are using only a constant amount of space.
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
