from ply import yacc
from uwu_lexer import UWULexer
from .ast_node import IdentifierNode, AssignmentNode, ConstantNode, BinaryOpNode, GenericNode
class UWUParser(object):
    def __init__(self, lexer=UWULexer):
        # Call and build lexer
        self.lex = lexer()
        self.lex.build()

        # store lexer tokens 
        self.tokens = self.lex.tokens        
        self.parser = yacc.yacc(module=self)

    
    def parse(self, text, dbg=True):
        return self.parser.parse(input=text,lexer=self.lex, debug=dbg)

    def p_error(self, p):
        # TODO update the syntax error message
        print("there was a syntax error")
    
    ######################--   LANGUAGE RULES   --######################

    precedence = (
        ('left', 'EQUAL'),
        ('left', 'OR'),
        ('left', 'AND'),
        ('left', 'IS', 'NOT'),
        ('left', 'GT', 'LT'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'MULT', 'DIVIDE', 'MOD'),
    )

    

    # def p_statements(self, p):
    #     '''
    #     statements  : statement statments
    #                 | statement
    #     '''
    #     p[0] = GenericNode(children=[p[1], p[2]])

    def p_statement(self, p):
        '''
        statement   : assign_stmnt
                    | expr_stmnt
        '''
        p[0] = GenericNode(children=[p[1]])
    
    def p_assign_statement(self, p):
        '''
        assign_stmnt    : identifier EQUAL expr_stmnt
        '''
        p[0] = AssignmentNode(p[2], children=[p[1], p[3]])

    def p_expr_statement(self, p):
        '''
        expr_stmnt  : binary_expr
                    | number_const
                    | identifier
        '''
        p[0] = GenericNode(children=[p[1]])

    
    def p_binary_expression(self, p):
        '''
        binary_expr   : expr_stmnt binary_op_math expr_stmnt
        '''
        # pass correct operation into binary operation node class
        p[0] = BinaryOpNode(p[2], children=[p[1], p[3]])
    

    def p_binary_op_math(self, p):
        '''
        binary_op_math  : PLUS
                        | MINUS
                        | MULT
                        | DIVIDE
                        | MOD   
        '''
        p[0] = p[1]

    def p_number_const(self, p):
        '''
        number_const    : NUMBER_CONST
        '''
        # TODO check token and identify if it is a constant
        p[0] = ConstantNode(children=[p[1]])


    def p_identifier(self, p):
        '''
        identifier  : ID
        '''
        p[0] = IdentifierNode(children=[p[1]])
        
    

    