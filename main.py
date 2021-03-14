from uwu_lexer import UwuLexer
from uwu_parser import UwuParser

# def error ():
#     pass
# t = UwuLexer(error_func=error)
# t.build()
# t.test(
#     '''
#     > 
#     '''
# )

# TODO issue with > symbol 
foo = UwuParser()
print(foo.parse(
    '''
    var a : int
    '''
))

