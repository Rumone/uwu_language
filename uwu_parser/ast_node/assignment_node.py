from .node import Node
from uwu_global import update_env

class AssignmentNode(Node):
    def __init__(self, root, children=[]):
        super().__init__(children)
        self.root = root

    def evaluate_node(self):
        # print('evaluation assignment')
        # node evaluation
        # In this node the first node is the left and the second
        # is the value
        update_env(self.children[0].evaluate_node(), self.children[1].evaluate_node())
        
        