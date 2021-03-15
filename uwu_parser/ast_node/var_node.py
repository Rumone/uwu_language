from .node import Node

class VarNode(Node):
    def __init__(self, children=[]):
        self.children = children
     
    def evaluate_node(self):
        return self.children[0]
