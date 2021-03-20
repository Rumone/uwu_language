from .node import Node

class IdentifierNode(Node):
    def __init__(self, children=[]):
        self.children = children
    
    def evaluate_node(self):
        return self.children[0]