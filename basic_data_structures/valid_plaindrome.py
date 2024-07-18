class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()

        arr = [i for i in s if ord(i) >= 97 and ord(i) <= 122  or ord(i) >= 48 and ord(i) <= 57]

        s = ''.join(arr)
        
        left, right = 0, len(s)-1
        
        while left <= right:
            if s[left] != s[right]:
                return False
            left +=1
            right -=1
        
        return True
