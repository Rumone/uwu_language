import ply.lex as lex
from ply.lex import TOKEN

class UwuLexer(object):
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
        'try': 'TRY',
        'catch': 'CATCH',
        'string': 'STRING',
        'int': 'INT',
        'float': 'FLOAT',
        'and': 'AND',
        'or': 'OR',
        'if': 'IF',
        'then': 'THEN',
        'else': 'ELSE',
        'elseif': 'ELSEIF',
        'func': 'FUNC'     
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
        'COMMENT'
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

    t_ignore = ' \t'


    # Regular expressions for the tokens created above
    identifier = r'[a-zA-Z][0-9a-zA-Z]*'

    escape_sequence_start_in_string = r"""(\\[0-9a-zA-Z._~!=&\^\-\\?'"])"""
    string_char = r"""([^"\\\n]|"""+escape_sequence_start_in_string+')'
    string_literal = '"'+string_char+'*"'

    integer = r'\d+'

    newline = r'\n+'


    def t_COMMENT(self, t):
        r'\#.*'
        pass

    @TOKEN(identifier)
    def t_ID(self, t):
        t.type = self.keywords.get(t.value, 'ID')
        return t

    @TOKEN(integer)
    def t_INT(self, t):
        t.value = int(t.value)
        return t

    @TOKEN(string_literal)
    def t_STRINGLITERAL(self, t):
        return t

    @TOKEN(newline)
    def t_newline(self, t):
        t.lexer.lineno += len(t.value)
    
    def t_error(self, t):
        # Prints the character that offended the lexer 
        print("[Error]:Please check the character '%s'👉👈" % t.value[0])
        # Skips to the other character so the lexer does not crash
        t.lexer.skip(1)
    
    def build(self, **kwargs):
        self.lexer = lex.lex(debug=True, module=self, **kwargs)
    
    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)