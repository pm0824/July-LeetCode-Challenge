'''
Write a program to find the n-th ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:
Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  
1 is typically treated as an ugly number.
n does not exceed 1690.
   Hint #1  
The naive approach is to call isUgly for every number until you reach the nth one. Most numbers are not ugly. Try to focus your effort on generating only the ugly ones.
   Hint #2  
An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
   Hint #3  
The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from three sorted lists: L1, L2, and L3.
   Hint #4  
Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).
'''

#Solution:

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [0] * n # To store ugly numbers 
  
        # 1 is the first ugly number 
        ugly[0] = 1
  
        # i2, i3, i5 will indicate indices for 2,3,5 respectively 
        i2 = i3 =i5 = 0
  
        # set initial multiple value 
        next_multiple_of_2 = 2
        next_multiple_of_3 = 3
        next_multiple_of_5 = 5
  
        # start loop to find value from ugly[1] to ugly[n] 
        for l in range(1, n): 
  
            # choose the min value of all available multiples 
            ugly[l] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5) 
  
            # increment the value of index accordingly 
            if ugly[l] == next_multiple_of_2: 
                i2 += 1
                next_multiple_of_2 = ugly[i2] * 2
  
            if ugly[l] == next_multiple_of_3: 
                i3 += 1
                next_multiple_of_3 = ugly[i3] * 3
  
            if ugly[l] == next_multiple_of_5:  
                i5 += 1
                next_multiple_of_5 = ugly[i5] * 5
  
        # return ugly[n] value 
        return ugly[-1] 
        
        
        
        
        
