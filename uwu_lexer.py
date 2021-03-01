import ply.lex as lex
from ply.lex import TOKEN

class UwuLexer(object):
    # keywords
    keywords = (
        'WHILE', 'NOT', 'IS', 'FOR', 'IN', 'RETURN', 'BREAK', 'CONTINUE', 
        'TRY', 'CATCH', 'STRING', 'INT', 'FLOAT', 'AND', 'OR', 'IF', 'THEN',
        'ELSE', 'ELSEIF', 'FUNCTION', 
    )

    # List of all tokens
    tokens = keywords + (
        # Identifiers
        'ID',

        # operators
        'PLUS', 'MINUS', 'MULT', 'DIVIDE', 'MOD',

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
    )

    # Regular expressions for the tokens created above
    identifier = r'[a-zA-Z][0-9a-zA-Z]*'

    escape_sequence_start_in_string = r"""(\\[0-9a-zA-Z._~!=&\^\-\\?'"])"""
    string_char = r"""([^"\\\n]|"""+escape_sequence_start_in_string+')'
    string_literal = '"'+string_char+'*"'

    integer = r'\d+'

    newline = r'\n+'

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

    # Assignment Regex
    t_EQUAL = r'\='

    t_ignore = ' \t'

    # Logical Operators
    t_AND = r'and'
    t_OR = r'or'

    @TOKEN(integer)
    def t_INT(self, t):
        t.value = int(t.value)
        return t

    @TOKEN(newline)
    def t_newline(self, t):
        t.lexer.lineno += len(t.value)
    
    def t_error(self, t):
        print("Illegal character")
        t.lexer.skip(1)
    
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
    
    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)