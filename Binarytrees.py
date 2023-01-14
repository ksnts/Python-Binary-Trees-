class BinarySearchTreenode:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreenode(data)
            
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreenode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else: 
                return False

    def IOtraversal(self):
        elements = []
        if self.left:
            elements += self.left.IOtraversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.IOtraversal()

        return elements

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self

    def POtraversal(self):
        elements = []
        if self.left:
            elements += self.left.POtraversal()
        if self.right:
            elements += self.right.POtraversal()

        elements.append(self.data)

        return elements

    def PRtraversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.PRtraversal()
        if self.right:
            elements += self.right.PRtraversal()

        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0 
        return self.data + left_sum + right_sum

def build_tree(elements):
    print("Building Binary Tree with your name:", elements)
    root = BinarySearchTreenode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    letters_tree2 = build_tree(['J', 'O', 'H', 'N', 'K', 'Y', 'L', 'L', 'E', 'M', 'S', 'A', 'N', 'T', 'O', 'S'])
    letters_tree2.delete('H')
    print("After deleting H",letters_tree2.IOtraversal())
    print("\n")

    letters_tree2 = build_tree(['J', 'O', 'H', 'N', 'K', 'Y', 'L', 'L', 'E', 'M', 'S', 'A', 'N', 'T', 'O', 'S'])
    letters_tree2.delete('K')
    print("After deleting K",letters_tree2.IOtraversal())
    print("\n")

    letters_tree2 = build_tree(['J', 'O', 'H', 'N', 'K', 'Y', 'L', 'L', 'E', 'M', 'S', 'A', 'N', 'T', 'O', 'S'])
    letters_tree2.delete('O')
    print("After deleting O",letters_tree2.IOtraversal())
    print("\n")

    
    letters = ['J', 'O', 'H', 'N', 'K', 'Y', 'L', 'L', 'E', 'M', 'S', 'A', 'N', 'T', 'O', 'S']

    letters_tree = build_tree(letters)
    print("Full name:", letters)
    print("\n")
    print("In-Order Traversal:", letters_tree.IOtraversal())
    print("\n")
    print("Pre-Order Traversal:", letters_tree.PRtraversal())
    print("\n")
    print("Post-Order Traversal:", letters_tree.POtraversal())
    print("\n")


    

