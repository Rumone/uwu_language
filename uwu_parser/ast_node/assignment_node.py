from .node import Node
from uwu_global import update_env

class AssignmentNode(Node):
    def __init__(self, root, builder, module, children=[]):
        super().__init__(builder, module, children)
        self.root = root

    def eval(self):
        # print('evaluation assignment')
        # node evaluation
        # In this node the first node is the left and the second
        # is the value
        update_env(self.children[0].eval(), self.children[1].eval())
        
        