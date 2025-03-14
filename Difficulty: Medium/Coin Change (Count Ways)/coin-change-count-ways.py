from functools import lru_cache
class Solution:
    def count(self, coins, amount):
        # code here
        coins=tuple(coins)
        @lru_cache(None)
        def helper(n,remaining_amt):
            if remaining_amt==0:
                return 1
            if remaining_amt<0 or n==0:
                return 0
            include=helper(n,remaining_amt-coins[n-1])
            exclude=helper(n-1,remaining_amt)
            return include+exclude
        
        return helper(len(coins),amount)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        coins = list(map(int, input().strip().split()))
        sum = int(input())
        ob = Solution()
        print(ob.count(coins, sum))

        print("~")

# } Driver Code Ends