#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def addTwoLists(self, num1, num2):
        # code here
        def rev(head):
            temp=head
            prev=None
            
            while temp:
                temp2=temp.next
                temp.next=prev
                prev=temp
                temp=temp2
            return prev
        
        
        l1=rev(num1)
        l2=rev(num2)
        head=l1
        prev=None
        c=0
        su=0
        while l1 and l2:
            su=c+l1.data+l2.data
            l1.data=su%10
            c=su//10
            prev=l1
            l1=l1.next
            l2=l2.next
        if l1 is not None or l2 is not None:
            if l2 is not None:
                prev.next=l2
            l1=prev.next
            while l1 is not None:
                su=c+l1.data
                prev=l1
                l1.data=su%10
                c=su//10
                l1=l1.next
        if c>0:
            prev.next=Node(c)
        
        head=rev(head)
        while head.data==0:
            head=head.next
        return head
        
            
            
            
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Node Class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()


if __name__ == '__main__':
    for _ in range(int(input())):

        arr1 = (int(x) for x in input().split())
        num1 = LinkedList()
        for i in arr1:
            num1.insert(i)

        arr2 = (int(x) for x in input().split())
        num2 = LinkedList()
        for i in arr2:
            num2.insert(i)

        res = Solution().addTwoLists(num1.head, num2.head)
        printList(res)
        print("~")

# } Driver Code Ends