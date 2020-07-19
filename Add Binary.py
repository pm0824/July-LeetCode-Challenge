'''
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
 
Constraints:
Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.
'''

#Solution 1:starting from last characters of two strings and find digit sum one by one. If sum becomes more than 1, then store carry for next digits.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res=""
        maxl = max(len(a), len(b)) 
  
        a = a.zfill(maxl)     #Adds 0 in the beginning
        b = b.zfill(maxl)  
        carry = 0
   
        for i in range(maxl - 1, -1, -1): 
            r = carry 
            r += 1 if a[i] == '1' else 0
            r += 1 if b[i] == '1' else 0
            res = ('1' if r % 2 == 1 else '0') + res 
            carry = 0 if r < 2 else 1      
          
        if carry !=0 : res = '1' + res
  
        return res.zfill(maxl) 
        
#Solution 2: 
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result += str(carry %2)
            carry //= 2

        return result[::-1]
        
        
        
