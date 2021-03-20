from .node import Node

class IdentifierNode(Node):
    def __init__(self, children=[]):
        super().__init__(children)
    
    def evaluate_node(self):
        return self.children[0]