from .node import Node
from uwu_global import find_value

class FuncCallNode(Node):
    def __init__(self, children=[]):
        super().__init__(children)

    def evaluate_node(self):
        function = find_value(self.children[0].evaluate_node())
        return function.evaluate_node()