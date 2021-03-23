from .node import Node
from uwu_global import find_value

class FuncCallNode(Node):
    def __init__(self, builder, module, children=[]):
        super().__init__(builder, module, children)

    def eval(self):
        function = find_value(self.children[0].eval())
        return function.eval()