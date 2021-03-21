from .node import Node
from llvmlite import ir


class IdentifierNode(Node):
    def __init__(self, builder, module, children=[]):
        super().__init__(builder, module, children)
    
    def evaluate_node(self):
        return self.children[0]

    def evaluate_codegen(self):
        pass