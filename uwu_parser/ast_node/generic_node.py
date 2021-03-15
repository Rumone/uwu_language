from .node import Node

class GenericNode(Node):
    def __init__(self, children=[]):
        super().__init__(children)

    def evaluate_node(self):
        # evaluate the expression and return the results
        return self.children[0].evaluate_node()