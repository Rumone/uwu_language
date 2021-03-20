from .node import Node

class PrintNode(Node):
    def __init__(self, children=[]):
        super().__init__(children)

    def evaluate_node(self):
        print(self.children[0].evaluate_node())