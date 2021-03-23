from .node import Node

class GenericNode(Node):
    def __init__(self, builder, module, children=[]):
        super().__init__(builder, module, children)

    def eval(self):
        child_eval = []
        # evaluate the expression and return the results
        if len(self.children) == 1:
            return self.children[0].eval()
        else:
            for child in self.children:
                child_eval.append(child.eval())
        return child_eval