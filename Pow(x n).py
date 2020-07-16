'''
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]

The main idea of solution is to use as much multiplications as possible, for example how can we evaluate x^20? We can just multiply x in loop 20 times, 
but we also can evaluate x^10 and multiply it by itself! Similarly, x^10 = x^5 * x^5. Now we have odd power, but it is not a problem, 
we evaluate x^5 = x^2 * x^2 * x. We also need to deal with some border cases, here is the full algorithm:

If we have very small value of x we can directly return 0, the smallest value of float is 1.175494 × 10^(-38).
If we have n = 0, return 1.
If we have negative power, return positive power of 1/x.
Now, we have two cases: for even and for odd n, where we evaluate power n//2.
Complexity: time complexity is O(log n), space complexity for this recursive algorithm is also O(log n), which can be reduced to O(1), 
if we use iterative approach instead.
'''
#Solution:

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if abs(x) < 1e-40: return 0 
        if n == 0: return 1
        
        if n < 0: return self.myPow(1/x, -n)
        half = self.myPow(x, n//2)
        print(half)
        if n % 2 == 0: 
            return half*half
        else: 
            return half*half*x
            
            
            
            
