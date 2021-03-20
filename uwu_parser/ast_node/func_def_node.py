from .node import Node
from uwu_global import update_env

class FuncDefNode(Node):
    def __init__(self, children=[]):
        super().__init__(children)

    def evaluate_node(self):
        update_env(self.children[0].evaluate_node(), self.children[1])