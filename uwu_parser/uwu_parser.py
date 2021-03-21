from ply import yacc
from uwu_lexer import UWULexer
from .ast_node import *
class UWUParser(object):
    def __init__(self, module, builder, printf, lexer=UWULexer):
        # Call and build lexer
        self.lex = lexer()
        self.lex.build()

        self.module = module
        self.builder = builder
        self.printf = printf

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

    def p_function_definition(self, p):
        '''
        func_def    : FUNC identifier LPAREN RPAREN ARROW LBRACE statements RBRACE
                    | LPAREN RPAREN ARROW LBRACE statements RBRACE
        '''
        if len(p) == 9:    
            p[0] = FuncDefNode(children=[p[2], p[7]])   
        else:
            p[0] = GenericNode(children=[p[5]])

    def p_statements(self, p):
        '''
        statements  : statement statements
                    | statement
        '''
        if len(p) > 2:
            p[0] = GenericNode(children=[p[1], p[2]])
        else:
            p[0] = GenericNode(children=[p[1]])
            
    def p_statement(self, p):
        '''
        statement   : assign_stmnt
                    | expr_stmnt
                    | func_call
                    | func_def
                    | if_stmnt
                    | print_stmnt
        '''
        p[0] = GenericNode(children=[p[1]])
    
    def p_assign_statement(self, p):
        '''
        assign_stmnt    : identifier EQUAL expr_stmnt
        '''
        p[0] = AssignmentNode(p[2], children=[p[1], p[3]])

    def p_func_call(self, p):
        '''
        func_call   : identifier LPAREN RPAREN
        '''
        p[0] = FuncCallNode(children=[p[1]])

    def p_if_stmnt(self, p):
        '''
        if_stmnt    : IF cond_stmnt LBRACE statements RBRACE
        '''
        p[0] = IfStatementNode(children=[p[2], p[4]])
    
    def p_print_stmnt(self, p):
        '''
        print_stmnt : PRINT LBRACKET string_const RBRACKET
        '''
        p[0] = PrintNode(children=[p[3]])

    def p_expr_statement(self, p):
        '''
        expr_stmnt  : binary_expr
                    | cond_stmnt
                    | operand
        '''
        p[0] = GenericNode(children=[p[1]]) 
    
    def p_binary_expression(self, p):
        '''
        binary_expr   : expr_stmnt binary_op_math expr_stmnt
        '''
        # pass correct operation into binary operation node class
        p[0] = BinaryOpNode(p[2], children=[p[1], p[3]])

    def p_cond_stmnt(self, p):
        '''
        cond_stmnt : operand binary_op_logic operand
        '''
        p[0] = ConditionStatementNode(p[2], children=[p[1],p[3]])
    

    def p_binary_op_math(self, p):
        '''
        binary_op_math  : PLUS
                        | MINUS
                        | MULT
                        | DIVIDE
                        | MOD   
        '''
        p[0] = p[1]

    def p_binary_op_logic(self, p):
        '''
        binary_op_logic : AND
                        | OR
                        | IS
                        | GT
                        | LT
        '''
        p[0] = p[1]

    
    def p_operand(self, p):
        '''
        operand : identifier 
                | number_const
        '''
        p[0] = GenericNode(children=[p[1]])

    def p_number_const(self, p):
        '''
        number_const    : NUMBER_CONST
        '''
        # TODO check token and identify if it is a constant
        Number(self.builder, self.module, p[1].value)
        p[0] = ConstantNode(children=[p[1]])
    
    def p_string_const(self, p):
        '''
        string_const    : STRINGLITERAL
        '''
        # TODO check token and identify if it is a constant
        p[0] = ConstantNode(children=[p[1]])


    def p_identifier(self, p):
        '''
        identifier  : ID
        '''
        p[0] = IdentifierNode(children=[p[1]])

    
    