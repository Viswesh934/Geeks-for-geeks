import heapq
class Solution:
	def kLargest(self, arr, k):
		# Your code here
		t=[0]*len(arr)
		for i in range(len(arr)):
		    t[i]=-1*arr[i]
		    
		heapq.heapify(t)
		p=[]
		c=0
		while(c<k):
		    r=heapq.heappop(t)
		    p.append(-1*r)
		    c+=1
		return p
		    
		    
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.kLargest(arr, k)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends