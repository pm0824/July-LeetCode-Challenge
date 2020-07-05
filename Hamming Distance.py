'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
'''
#Solution 1: Comparing each bit 

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xx=bin(x).replace("0b", "") 
        yy=bin(y).replace("0b", "") 
        lx=len(xx)
        ly=len(yy)
        l=max(lx,ly)
        if(lx>ly):
            s='0'*(lx-ly)
            yy=s+yy
        else:
            s='0'*(ly-lx)
            xx=s+xx
       
        c=0
        for i in range(l):
            if(xx[i]!=yy[i]):
                c+=1
        return c
        
#Solution 2:
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')
        
        
        
        
        
