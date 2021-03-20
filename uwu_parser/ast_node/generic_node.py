from .node import Node

class GenericNode(Node):
    def __init__(self, children=[]):
        super().__init__(children)

    def evaluate_node(self):
        child_eval = []
        # evaluate the expression and return the results
        if len(self.children) == 1:
            return self.children[0].evaluate_node()
        else:
            for child in self.children:
                child_eval.append(child.evaluate_node())
        return child_eval