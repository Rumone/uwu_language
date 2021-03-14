from uwu_parser import UWUParser

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
foo = UWUParser()
print(foo.parse(
    '''
    var a : int
    '''
))

