class Node:
    def __init__(self) -> None:
        self.name = None
        self.child = [None,None,None]
        self.sibling = None
        self.line = None
        self.node_kind = None
    
    def preorden(self):
        print(self.name)
        for node in self.child:
            if node == None:
                break
            else:
                node.preorden()
    
    def to_dict(self):
        children = []
        for node in self.child:
            if node == None:
                break
            else:
                children.append(node.to_dict())
        
        if children == []:
            return {
                "name": self.name
            }
        else:
            return {
                "name": self.name,
                "children": children
            }