"""Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""
class Solution:
    def reverseKGroup(self, head, k):
        # Code here
        def rev(node):
            temp=node
            prev=None
            while(temp):
                temp2=temp.next
                temp.next=prev
                prev=temp
                temp=temp2
            return prev
            
        def kNode(node):
            c=1
            while(node and node.next and  c<k):
                node=node.next
                c+=1
            return node
        temp=head
        
        while(temp):
            knode=kNode(temp)
            nextnode=knode.next
            knode.next=None
            
            rev(temp)
            
            if temp==head:
                head=knode
            else:
                prev.next=knode
            prev=temp
            temp=nextnode
            
                
            
        return head

#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


if __name__ == '__main__':
    t = int(input())  # Number of test cases
    while t > 0:
        llist = LinkedList()

        # Read list values and push them to the LinkedList
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)

        k = int(input())  # Size of the group for reversal
        ob = Solution()
        new_head = ob.reverseKGroup(llist.head, k)
        llist.head = new_head
        llist.printList()  # Print the modified linked list
        t -= 1

        print("~")

# } Driver Code Ends