class Node:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.code = ""
        self.left = None
        self.right = None

    def isLeaf(self):
        return not self.left and not self.right

    def updateCode(self, addedChar):
        self.code = addedChar + self.code
        if self.left:
            self.left.updateCode(addedChar)
        if self.right:
            self.right.updateCode(addedChar)
