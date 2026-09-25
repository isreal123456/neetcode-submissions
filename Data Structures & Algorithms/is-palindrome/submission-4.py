class Solution:
    def isPalindrome(self, s: str) -> bool:

        l = list(re.sub(r'[^a-zA-Z0-9]', '', s).lower())
        
       
        return l == l[::-1]
           
