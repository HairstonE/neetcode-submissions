class Node:
    def __init__(self, val= "", end=False):
        self.val = val
        self.next = dict()
        self.end = end
    def __str__(self):
        return f"{self.val}, {self.next}, {self.end}"
class PrefixTree:

    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        node = self.root
        for l in word:
            if l in node.next:
                node = node.next[l]
            else:
                next = Node(l)
                node.next[l] = next
                node = next
        node.end = True
        # print(self.root)

    def search(self, word: str) -> bool:
        node = self.root
        # print(node)
        for l in word:
            if l not in node.next:
                return False
            node = node.next[l]
        
        return node.end == True
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for l in prefix:
            if l not in node.next:
                return False
            node = node.next[l]
        return True
        
        