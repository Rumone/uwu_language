from .node import Node
from uwu_global import update_env

class FuncDefNode(Node):
    def __init__(self, builder, module, children=[]):
        super().__init__(builder, module, children)

    def eval(self):
        update_env(self.children[0].eval(), self.children[1])