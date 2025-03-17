class Solution:
    def isSubsetSum (self, arr, s):
        # code here 
        dp= [-1 for _ in range(s+1)]
        dp[0]=0
        
        for i in range(len(arr)):
            if arr[i]>s:
                continue
            for j in range(arr[i],s+1):
                if dp[j]==-1 and dp[j-arr[i]]!=-1 and dp[j-arr[i]]!=i+1:
                    dp[j]=i+1
        return dp[s]!=-1
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(arr, sum) == True:
            print("true")
        else:
            print("false")

        print("~")

# } Driver Code Ends