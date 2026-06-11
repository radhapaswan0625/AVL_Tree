#A single node in the AVL Tree
class Node:
    def __init__(self, key):
        self.key = key               #the value stored in this node
        self.left = None             #pointer to left child (smaller value)
        self.right = None            #pointer to right child(larger value)
        self.height = 1              #height of this node, start at 1

#The AVL Tree itself
class AVLTree:
    def __init__(self):
        self.root = None             #tree is empty at the start , no nodes yet 


    #returns height of a node (0 if node is empty)
    def get_height(self, node):
        if not node:
            return 0
        return node.height
    
    #returns balance factor = left height minus right height 
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    #LL case - rotate right to fix balance 
    def rotate_right(self, z):
        y = z.left                      # y becomes new root
        T3 = y.right                    # save y's right subtree

        # perform rotation
        y.right = z
        z.left = T3

        #update heights (z first, then y)
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))


        return y                          # y is the new root now
    
    # RR case - rotate left fo fix balance
    def rotate_left(self, z):
        y = z.right                       # y becomes new root
        T2 = y.left                       # save y's left subtree

        #perform rotation
        y.left = z
        z.right = T2

        # update heights (z first, then y )
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y                            # y is the new root now 
    
    # insert a key into the AVL tree
    def insert(self, root, key):
        #STEP 1 - normal BST insert 
        if not root:
            return Node(key)                 # empty spot found, place node here
        if key < root.key:
            root.left = self.insert(root.left, key)           # go left
        elif key > root.key:
            root.right = self.insert(root.right, key)         # go right
        else:
            return root                                       # duplicate key, ignore it 
        
        # STEP 2 - update height of current node
        root.height = 1 +max(self.get_height(root.left), self.get_height(root.right))

        #STEP 3 - check balance
        balance = self.get_balance(root)

        # LL case
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)
        
        # RR case
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)
        
        # LR case
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        
        # RL case 
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        
        return root

    # search for a key in the tree
    def search(self, root, key):
        # base case - node is empty or key found
        if not root:
            return False            # key not found
        if root.key == key:
            return True             # key found
        
        # go left if key is smaller
        if key < root.key:
            return self.search(root.left, key)
        
        # go right if key is larger
        return self.search(root.right, key)
    
    # find the node with smallest key in a subtree
    def get_min_node(self, node):
        if node.left is None:
            return node
        return self.get_min_node(node.left)
    
    # delete a key from the tree
    def delete(self, root, key):
        # SETP 1 - normal BST delete
        if not root:
            return root                 #key not found
        
        if key < root.key:
            root.left = self.delete(root.left, key)             # go left 
        elif key > root.key:
            root.right = self.delete(root.right, key)           # go right
        else:
            # founde the node to delete 

            # Case 1 & 2 - one child or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Case 3 - two children
            successor = self.get_min_node(root.right)                # find smallest in right 
            root.key = successor.key                                 # copy successor key
            root.right = self.delete(root.right, successor.key)      # delete successor

        # STEP 2 - update height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # STEP 3 - check balance and rotate if neede
        balance = self.get_balance(root)

        # LL case
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)
        
        # LR case
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        
        # RR case
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)
        
        # RL case
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        
        return root
    
    # update an existing key with a new key
    def update(self, root, old_key, new_key):
        # check if old key exists
        if not self.search(root, old_key):
            print("key", old_key, "not found!")
            return root
        
        # check if new key already exists
        if self.search(root, new_key):
            print("key", new_key, "already exists!")
            return root
        
        # delete old key and insert new key
        root = self.delete(root, old_key)
        root = self.insert(root, new_key)
        print("Updated", old_key, "to", new_key)
        return root
    
    # in-order traversal - left, root, right (gives sorted output)
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.key, end=" ")
        self.inorder(root.right)

    # pre-order traversal - root, left, right
    def preorder(self, root):
        if not root:
            return
        print (root.key, end= " ")
        self.preorder(root.left)
        self.preorder(root.right)

    # print height and balance factor of each node (in - order)
    def print_node_info(self, root):
        if not root:
            return
        self.print_node_info(root.left)
        print("Key:", root.key, "| Height:", root.height, "| Balance Factor:", self.get_balance(root))
        self.print_node_info(root.right) 

    # Visualize tree structure sideways in terminal 
    def print_tree(self, root, level=0, prefix="Root:"):
        if not root:
            return
        print(" " * (level * 6) + prefix + str(root.key))
        
        # if root.left or root.right:
        if root.right:
            self.print_tree(root.right, level + 1, "R--- ")
        if root.left:
            self.print_tree(root.left, level + 1, "L--- ")


# ============================================
#         REGULAR BST (NO BALANCING)
# ============================================

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # get height of a node
    def get_height(self, node):
        if not node:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))

    # insert without balancing - no rotations
    def insert(self, root, key):
        if not root:
            return BSTNode(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root

    # visualize tree structure
    def print_tree(self, root, level=0, prefix="Root: "):
        if not root:
            return
        print(" " * (level * 6) + prefix + str(root.key))
        if root.right:
            self.print_tree(root.right, level + 1, "R--- ")
        if root.left:
            self.print_tree(root.left, level + 1, "L--- ")

tree = AVLTree()

# ---- INSERT ----
print("=" * 40)
print("INSERTING KEYS")
print("=" * 40)
tree.root = tree.insert(tree.root, 30)
tree.root = tree.insert(tree.root, 15)
tree.root = tree.insert(tree.root, 50)
tree.root = tree.insert(tree.root, 10)
tree.root = tree.insert(tree.root, 20)
tree.root = tree.insert(tree.root, 40)
tree.root = tree.insert(tree.root, 60)
print("Inserted: 30, 15, 50, 10, 20, 40, 60")
print("\nTree Structure:")
tree.print_tree(tree.root)

print("\nIn-order traversal:")
tree.inorder(tree.root)
print("\nPre-order traversal:")
tree.preorder(tree.root)

print("\n\nNode Info:")
tree.print_node_info(tree.root)

# --- SEARCH ---
print("\n" + "=" * 40)
print("SEARCHING KEYS")
print("=" * 40)
print("Search 20:", tree.search(tree.root, 20))
print("Search 99:", tree.search(tree.root, 99))

# --- UPDATE ---
print("\n" + "=" * 40)
print("UPDATING KEY")
print("=" * 40)
tree.root = tree.update(tree.root, 15, 25)
print("\nTree Structure after update:")
tree.print_tree(tree.root)
print("\nIn-order after update:")
tree.inorder(tree.root)

# --- DELETE ---
print("\n\n" + "=" * 40)
print("DELETING KEY")
print("=" * 40)
tree.root = tree.delete(tree.root, 30)
print("Deleted 30")
print("\nTree Structure after delete:")
tree.print_tree(tree.root)

print("\nIn-order after delete:")
tree.inorder(tree.root)
print("\nPre-order after delete:")
tree.preorder(tree.root)

# ============================================
#      COMPARISON: AVL TREE VS REGULAR BST
# ============================================

print("\n\n" + "=" * 40)
print("COMPARISON: AVL TREE VS REGULAR BST")
print("=" * 40)

# insert same keys in same order
keys = [10, 20, 30, 40, 50]

# AVL Tree
avl = AVLTree()
for k in keys:
    avl.root = avl.insert(avl.root, k)

# Regular BST
bst = BST()
for k in keys:
    bst.root = bst.insert(bst.root, k)

print("\nInserting keys in order: 10, 20, 30, 40, 50")

print("\nAVL Tree Structure:")
avl.print_tree(avl.root)
print("AVL Tree Height:", avl.get_height(avl.root))

print("\nRegular BST Structure:")
bst.print_tree(bst.root)
print("Regular BST Height:", bst.get_height(bst.root))

print("\nConclusion:")
print("AVL Tree Height:", avl.get_height(avl.root), "← always balanced!")
print("Regular BST Height:", bst.get_height(bst.root), "← can become a straight line!")



    


    
        
        




