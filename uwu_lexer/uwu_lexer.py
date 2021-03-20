import ply.lex as lex
from ply.lex import TOKEN

import logging

# NOTE
# The order the token is defined in will determine if it is recognized
# Therefore, if the integer is defined before the float then it will not parse
# The float properly

class UWULexer(object):
    def __init__(self):
        pass

    def build(self, **kwargs):
        self.lexer = lex.lex(debug=False, module=self, **kwargs)
    
    def input(self, data):
        self.lexer.input(data)

    def token(self):
        self.last_token = self.lexer.token()
        return self.last_token
    
    def find_tok_column(self, token):
        """ Find the column of the token in its line.
        """
        last_cr = self.lexer.lexdata.rfind('\n', 0, token.lexpos)
        return token.lexpos - last_cr

    ######################--   PRIVATE   --######################

    def _error(self, msg, token):
        location = self._make_tok_location(token)
        print(msg, '[row]', location[0], '[col]', location[1])
        self.lexer.skip(1)

    # function returns coords of offending token
    def _make_tok_location(self, token):
        return (token.lineno, self.find_tok_column(token))


    ######################--   LANGUAGE TOKENS   --######################

    # keywords
    keywords = {
        'while':'WHILE',
        'for': 'FOR',
        'not': 'NOT',
        'is': 'IS',
        'in': 'IN',
        'return': 'RETURN',
        'break': 'BREAK',
        'continue': 'CONTINUE',
        'print': 'PRINT',
        'var': 'VAR',
        'string': 'STRING',
        'int': 'INT',
        'float': 'FLOAT',
        'and': 'AND',
        'or': 'OR',
        'if': 'IF',
        'else': 'ELSE',
        'elseif': 'ELSEIF',
        'func': 'FUNC',   
        'true': 'TRUE',   
        'false': 'FALSE',   
    }

    # List of all tokens
    tokens = list(keywords.values()) + [
        # Identifiers
        'ID',

        # operators
        'PLUS', 'MINUS', 'MULT', 'DIVIDE', 'MOD',

        # Arrow
        'ARROW',

        # Assignment
        'EQUAL',

        # Delimiters
        'LPAREN', 'RPAREN',
        'LBRACKET', 'RBRACKET',
        'LBRACE', 'RBRACE',
        'COMMA', 'PERIOD',
        'SEMI', 'COLON',

        # String literal
        'STRINGLITERAL',

        # Comment token
        'COMMENT',

        # conditionals
        'GT',
        'LT',

        # numberical token
        'NUMBER_CONST'
    ]


    # operators Regex
    t_PLUS = r'\+'
    t_MINUS = r'\-'
    t_MULT = r'\*'
    t_DIVIDE = r'\/'
    t_MOD = r'\%'    

    # Delimiter Regex
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LBRACKET = r'\['
    t_RBRACKET = r'\]'
    t_LBRACE = r'\{'
    t_RBRACE = r'\}'
    t_COLON = r'\:'
    t_SEMI = r'\;'
    t_COMMA = r'\,'

    # Assignment Regex
    t_EQUAL = r'\='

    # Arrow Syntax
    # Used to assign function
    t_ARROW = r'->'

    t_LT = r'\<'
    t_GT = r'\>'

    t_ignore = ' \t'


    # Regular expressions for the tokens created above
    identifier = r'[a-zA-Z][0-9a-zA-Z]*'

    escape_sequence_start_in_string = r"""(\\[0-9a-zA-Z._~!=&\^\-\\?'"])"""
    string_char = r"""([^"\\\n]|"""+escape_sequence_start_in_string+')'
    string_literal = '"'+string_char+'*"'

    newline = r'\n+'

    
    number_constant = r'([+-]?([0-9]+[.])?[0-9]+)'

    def t_COMMENT(self, t):
        r'\☁️.*'
        pass

    @TOKEN(identifier)
    def t_ID(self, t):
        t.type = self.keywords.get(t.value, 'ID')
        return t
        
    @TOKEN(number_constant)
    def t_NUMBER_CONST(self, t):
        if "." in t.value:
            t.value = float(t.value)
        else:
            t.value = int(t.value)
        return t

    @TOKEN(string_literal)
    def t_STRINGLITERAL(self, t):
        return t

    @TOKEN(newline)
    def t_newline(self, t):
        t.lexer.lineno += len(t.value)
    
    # TODO update error function
    def t_error(self, t):
        # Prints the character that offended the lexer 
        msg = "[Error]:Please check the character '%s'👉👈" 
        # Skips to the other character so the lexer does not crash
        self._error(msg=msg, token=t)

    


# When testing
# When the executed from this file a repl is generated to given tester an interface
# To identify the use of certain tokens in the laguage

if __name__ == '__main__':
    # Initialize lex analyzer
    lexer = UWULexer()
    lexer.build()


    def find_token(str):
        lexer.input(s)    
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(tok)

    # Generates REPL 
    # Prints response to user
    logging.basicConfig(format='[%(levelname)s 🌜]-%(message)s', level=logging.INFO)
    logging.info("Running from tokenizer")
    while True:
        try:
            s = input('🤔-> ')
        except EOFError:
            break
        except KeyboardInterrupt:
            break
        find_token(s)

    