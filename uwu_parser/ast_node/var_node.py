from .node import Node

class VarNode(Node):
    def __init__(self, builder, module, children=[]):
        super().__init__(self, builder, module)
     
    def eval(self):
        return self.children[0]
