from .node import Node

class ConditionStatementNode(Node):
    def __init__(self,children=[]):
        self.children = children
    
    def evaluate_node(self):
        for child in children:
            child.evaluate_node()
            print(child)
        return children