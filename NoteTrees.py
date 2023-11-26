     1
      \
       2
        \
         5
        /  \
       3    6
        \
         4  

def preOrder(root):
    #Write your code here
    if root != None:
        print(root.info, end=' ')
        preOrder(root.left)
        preOrder(root.right)
> 1 2 5 3 4 6 
        
        
def postOrder(root):
    #Write your code here
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.info, end=' ')
> 4 3 6 5 2 1 


def inOrder(root):
    #Write your code here
    if root:
        inOrder(root.left)
        print(root.info, end=" ")
        inOrder(root.right)
> 1 2 3 4 5 6 


def height(root):
    if root == None:
        return -1
    else:
        return 1 + max( height(root.left), height(root.right) )
> 4
Note: The height of binary tree with single node is taken to be 0 and the 
height of the empty binary tree is taken to be -1.


# 廣度優先搜尋 Breadth First Search，BSF
def levelOrder(root):
    queue = []
    queue.append(root)
    result = []
    while(len(queue)>0):
        node = queue.pop(0)
        result.append(node.info)
        print(node.info)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
> [1, 2, 5, 3, 6, 4]


# 深度優先搜尋 Depth First Search, DFS (右側優先)
def DFS(root):
    queue = []
    queue.append(root)
    result = []
    while(len(queue)>0):
        node = queue.pop()
        result.append(node.info)
        print(node.info)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
> [1, 2, 5, 6, 3, 4]


# 深度優先搜尋 Depth First Search, DFS (左側優先)
def DFS(root):
    queue = []
    queue.append(root)
    result = []
    while(len(queue)>0):
        node = queue.pop()
        result.append(node.info)
        print(node.info)
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
    return result
> [1, 2, 5, 3, 4, 6]


# 最近公共祖先 (Lowest common ancestor)
def lca(root, v1, v2):
  #Enter your code here
    while root:
        if root.info > v1 and root.info > v2:
            root = root.left
        elif root.info < v1 and root.info < v2:
            root = root.right
        else:
            break
    return root

lca(tree.root, 4, 6).info
> 5


######

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
###

tree = BinarySearchTree()
t = 6

arr = [1, 2, 5, 3, 6, 4]

for i in range(t):
    tree.create(arr[i])

inOrder(tree.root)


