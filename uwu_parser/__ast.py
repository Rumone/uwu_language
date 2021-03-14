class Node:
    def children(self):
        '''
        List of all the children that are nodes
        '''
        pass

# Operations available in language defined and inherits node class
class Assignment(Node):
    '''
    op: operator
    lvalue: left value
    rvalue: right value
    coord: current coordinate
    '''
    # default coord value is none if nothing is passed in
    def __init__(self, op, lvalue, rvalue, coord=None):
        self.op = op
        self.lvalue = lvalue
        self.rvalue = rvalue
        self.coord = coord
    
    def children(self):
        nodelist = []
        if self.lvalue is not None: nodelist.append(('lvalue', self.lvalue))
        if self.rvalue is not None: nodelist.append(('rvalue', self.rvalue))

    def __iter__(self):
        if self.lvalue is not None:
            yield  self.lvalue
        if self.rvalue is not None:
            yield  self.rvalue

