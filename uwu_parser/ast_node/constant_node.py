from .node import Node

class ConstantNode(Node):
    def __init__(self, builder, module, children=[]):
        super().__init__(builder, module, children)
     
    def eval(self):
        return self.children[0]
