
class Solution:
    def maxLength(self, s):
        # code here
        st=[]
        maxlen=0
        st.append(-1)
        for i in range(len(s)):
            if s[i]=="(" or len(st)==0:
                st.append(i)
            else:
                st.pop()
                if len(st)==0:
                    st.append(i)
                else:
                    maxlen=max(maxlen,i-st[len(st)-1])
        return maxlen
            


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.maxLength(S))
        print("~")

# } Driver Code Ends