class Solution:
	def isWordExist(self, mat, word):
		#Code here
		def dfs(mat,word,x,y,z):
		    n=len(mat)
		    m=len(mat[0])
		    
		    if z==len(word):
		        return True
		    
		    if x<0 or y<0 or x>=n or y>=m:
		        return False
		     
		    if mat[x][y]==word[z]:
		        temp=mat[x][y]
		        mat[x][y]='#'
		        
		        res=(dfs(mat,word,x-1,y,z+1) or dfs(mat,word,x,y+1,z+1) or dfs(mat,word,x,y-1,z+1) or dfs(mat,word,x+1,y,z+1))
		        mat[x][y]=temp
		        return res
		    return False
		   
		for i in range(len(mat)):
		    for j in range(len(mat[0])):
		        if mat[i][j]==word[0]:
		            if dfs(mat,word,i,j,0):
		                return True
		return False 
		 
		    


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for tt in range(T):
        n = int(input())
        m = int(input())
        mat = []
        for i in range(n):
            a = list(input().strip().split())
            b = []
            for j in range(m):
                b.append(a[j][0])
            mat.append(b)
        word = input().strip()
        obj = Solution()
        ans = obj.isWordExist(mat, word)
        if ans:
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends