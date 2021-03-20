from .node import Node

class ConditionStatementNode(Node):
    def __init__(self,logic_op,children=[]):
        self.children = children
        self.logic_op = logic_op

    
    def evaluate_node(self):
        pass