# lextab.py. This file automatically created by PLY (version 3.11). Don't edit!
_tabversion   = '3.10'
_lextokens    = set(('AND', 'ARROW', 'BREAK', 'CATCH', 'COLON', 'COMMA', 'COMMENT', 'CONTINUE', 'DIVIDE', 'ELSE', 'ELSEIF', 'EQUAL', 'FLOAT', 'FOR', 'FUNC', 'ID', 'IF', 'IN', 'INT', 'IS', 'LBRACE', 'LBRACKET', 'LPAREN', 'MINUS', 'MOD', 'MULT', 'NOT', 'OR', 'PERIOD', 'PLUS', 'RBRACE', 'RBRACKET', 'RETURN', 'RPAREN', 'SEMI', 'STRING', 'STRINGLITERAL', 'THEN', 'TRY', 'WHILE'))
_lexreflags   = 64
_lexliterals  = ''
_lexstateinfo = {'INITIAL': 'inclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_COMMENT>\\#.*)|(?P<t_ID>[a-zA-Z][0-9a-zA-Z]*)|(?P<t_INT>\\d+)|(?P<t_STRINGLITERAL>"([^"\\\\\\n]|(\\\\[0-9a-zA-Z._~!=&\\^\\-\\\\?\'"]))*")|(?P<t_newline>\\n+)|(?P<t_ARROW>->)|(?P<t_COLON>\\:)|(?P<t_COMMA>\\,)|(?P<t_DIVIDE>\\/)|(?P<t_EQUAL>\\=)|(?P<t_LBRACE>\\{)|(?P<t_LBRACKET>\\[)|(?P<t_LPAREN>\\()|(?P<t_MINUS>\\-)|(?P<t_MOD>\\%)|(?P<t_MULT>\\*)|(?P<t_PLUS>\\+)|(?P<t_RBRACE>\\})|(?P<t_RBRACKET>\\])|(?P<t_RPAREN>\\))|(?P<t_SEMI>\\;)', [None, ('t_COMMENT', 'COMMENT'), ('t_ID', 'ID'), ('t_INT', 'INT'), ('t_STRINGLITERAL', 'STRINGLITERAL'), None, None, ('t_newline', 'newline'), (None, 'ARROW'), (None, 'COLON'), (None, 'COMMA'), (None, 'DIVIDE'), (None, 'EQUAL'), (None, 'LBRACE'), (None, 'LBRACKET'), (None, 'LPAREN'), (None, 'MINUS'), (None, 'MOD'), (None, 'MULT'), (None, 'PLUS'), (None, 'RBRACE'), (None, 'RBRACKET'), (None, 'RPAREN'), (None, 'SEMI')])]}
_lexstateignore = {'INITIAL': ' \t'}
_lexstateerrorf = {'INITIAL': 't_error'}
_lexstateeoff = {}
