from ply import yacc
from uwu_lexer import UWULexer

import ast

class UWUParser(object):
    def __init__(self, lexer=UWULexer):
        self.uwulex = lexer(
            error_func=self.lex_error_func
        )

        # TODO Identify what the options to this function means
        self.uwulex.build(
            optimize=True,
        )

        self.tokens = self.uwulex.tokens        
        self.uwuparser = yacc.yacc(module=self)

    
    def parse(self, text):
        self.uwuparser.parse(
            input=text,lexer=self.uwulex, debug=True
        )

    # TODO create better function definition for lex analysis function error
    def lex_error_func(self, msg=None, line=None, column=None):
        print("[Error]:Please check the character '%s'👉👈")

    
    precedence = (
        ('left', 'OR'),
        ('left', 'AND'),
        ('left', 'IS', 'NOT'),
        ('left', 'GT', 'LT'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'MULT', 'DIVIDE', 'MOD'),
    )

    def p_statement(self, p):
        '''
        statement   : expression
                    | assignment
        '''
        p[0] = p[1]
        return p[0]

    def p_assignment(self, p):
        '''
        assignment  : identifier EQUAL expression
        '''
        p[0] = ('assignment', p[2], p[1], p[3])

    def p_var_init(self, p):
        '''
        var_init  : decl EQUAL expression
        '''
        p[0] = ('variable_initialization', p[2], p[1], p[3])

        
    def p_decl(self, p):
        '''
        decl    : VAR identifier COLON decl_type
                | VAR identifier   
        '''
        if len(p) >= 2:
            # declared with data type
            p[0] = ('typed_decl', p[1], p[2], p[3], p[4])
        else: 
            p[0] = ('decl', p[1], p[2]) 

    def p_decl_type(self, p):
        '''
        decl_type   : INT 
                    | FLOAT 
                    | STRING
        '''
        p[0] = p[1]


    def p_expression(self, p):
        '''
        expression  : binary_expression
        '''
        p[0] = p[1]
        # print(p[0])


    def p_binary_expression(self, p):
        '''
        binary_expression   : binary_expression PLUS binary_expression
                            | binary_expression MINUS binary_expression 
                            | binary_expression MULT binary_expression 
                            | binary_expression DIVIDE binary_expression 
                            | binary_expression MOD binary_expression 
                            | binary_expression AND binary_expression 
                            | binary_expression OR binary_expression 
                            | binary_expression IS binary_expression 
                            | binary_expression NOT binary_expression 
                            | binary_expression GT binary_expression 
                            | binary_expression LT binary_expression
                            | LPAREN binary_expression RPAREN 
                            | identifier 
        '''
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = ('binary_expression', p[2], p[1], p[3])

    def p_identifier(self, p):
        '''
        identifier  : ID
        '''
        p[0] = p[1]


    def p_error(self, p):
        # update the syntax error message
        print("there was a syntax error")

        
