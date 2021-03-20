from .node import Node

class IfStatementNode(Node):
    def __init__(self, children=[]):
        super().__init__(children)
    
    def evaluate_node(self):
        condition, instructions = (self.children[0], self.children[1])
        if bool(condition.evaluate_node()):
            instructions.evaluate_node()
        return

