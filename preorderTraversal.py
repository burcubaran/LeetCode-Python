WITH RECURSION:

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
         
         
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        alist=[]
        if not root:
            return alist
        else:
            return self.helper(root, alist)
        
    def helper(self, root, alist):
        if root:
            alist.append(root.val)
            self.helper(root.left, alist)
            self.helper(root.right, alist)
        return alist


WITHOUT RECURSION: STACK

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)        
         
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        s=Stack()
        if not root:
            return []
        else:
            alist=[]
            s.push(root)
            while s.size()>0:
                current=s.pop()
                alist.append(current.val)
                if current.right:
                    s.push(current.right)
                if current.left:
                    s.push(current.left)
                    
        return alist
