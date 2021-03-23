from .node import Node
from uwu_global import update_env, find_value

class ConditionStatementNode(Node):
    def __init__(self, logic_op, builder, module,children=[]):
        super().__init__(builder, module, children)
        self.logic_op = logic_op

    
    def eval(self):
        lval, rval = (self.children[0].eval(), self.children[1].eval())
        
        # get the actual value
        if (type(lval) is str):
            lval = find_value(lval)
        
        if (type(rval) is str):
            rval = find_value(rval)
            
        if self.logic_op == 'and':
            return (bool(lval) and bool(rval))
        elif self.logic_op == 'or':
            return (bool(lval) or bool(rval))
        elif self.logic_op == 'is':
            return (lval is rval)
        elif self.logic_op == '>':
            return (lval > rval)
        elif self.logic_op == '<':
            return (lval < rval)
        
        
        return True



# RULES
# any number thats not 0 will give true
# therefore 1 to infinity is true 
# 0 will return false
# any number and with 0 evaluation will atomatically be false
# an identifier is only another when the value in the env global file is the same as the other
# We all know how greater than and equal works