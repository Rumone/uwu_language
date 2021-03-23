from .node import Node

class IfStatementNode(Node):
    def __init__(self, builder, module, children=[]):
        super().__init__(builder, module, children)
    
    def eval(self):
        condition, instructions = (self.children[0], self.children[1])
        if bool(condition.eval()):
            instructions.eval()
        return

