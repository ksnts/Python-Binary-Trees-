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
    root = BinarySearchTreenode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    
    letters = ['J', 'O', 'H', 'N', 'K', 'Y', 'L', 'L', 'E', 'M', 'S', 'A', 'N', 'T', 'O', 'S']

    letters_tree = build_tree(letters)
    print("Full name:", letters)
    print("In-Order Traversal:", letters_tree.IOtraversal())
    print("Pre-Order Traversal:", letters_tree.PRtraversal())
    print("Post-Order Traversal:", letters_tree.POtraversal())


    

