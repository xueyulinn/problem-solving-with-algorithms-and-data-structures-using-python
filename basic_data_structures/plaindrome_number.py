class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = str(x)

        arr = [i for i in number]

        left, right = 0, len(arr)-1

        while left < right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1
            
        return True
