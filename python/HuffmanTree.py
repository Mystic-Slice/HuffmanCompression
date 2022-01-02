from Node import Node
class HuffmanTree:
    def __init__(self):
        self.root = None

    def createRoot(self, data, freq):
        self.root = Node(data, freq)

    def fromData(data, freq):
        newTree = HuffmanTree()
        newTree.createRoot(data, freq)
        return newTree

    def fromTrees(left, right):
        newTree = HuffmanTree()
        newTree.createRoot('\0', left.root.freq + right.root.freq)
        newTree.root.left = left.root
        newTree.root.right = right.root

        newTree.root.left.updateCode('0')
        newTree.root.right.updateCode('1')
        return newTree

    def __lt__(self, rhs):
        return self.root.freq < rhs.root.freq

    def characterCodes(self):
        charCodeMap = {}
        dfsStack = []
        dfsStack.append(self.root)
        while len(dfsStack):
            node = dfsStack.pop()
            if(node.isLeaf()):
                charCodeMap[node.data] = node.code
            else:
                dfsStack.append(node.left)
                dfsStack.append(node.right)
        
        return charCodeMap