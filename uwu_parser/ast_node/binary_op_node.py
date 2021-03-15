from .node import Node

from uwu_global import find_value

class BinaryOpNode(Node):
    def __init__(self, operation, children=[]):
        super().__init__(children)
        self.op = operation

    def evaluate_node(self):
        # evaluate the expression and return the results
        (lvalue, rvalue) = self._evaluate_leaves()
        if self.op == '+':
            result = lvalue + rvalue
        elif self.op == '-':
            result = lvalue - rvalue
        elif self.op == '*':
            result = lvalue * rvalue
        elif self.op == '/':
            result = lvalue / rvalue
        elif self.op == '%':
            result = lvalue % rvalue
        else:
            # TODO handle error here
            result = 0

        return result
    
    # TODO update function to be more pythonic
    def _evaluate_leaves(self):
        leaves = []
        for child in self.children:
            child_value = child.evaluate_node()
            if type(child_value) is str:
                child_value = find_value(child_value)
            leaves.append(child_value)
        return tuple(leaves)