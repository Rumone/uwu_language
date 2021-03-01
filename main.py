from uwu_lexer import UwuLexer

t = UwuLexer()
t.build()
t.test(
    '''
    var x:int=12;
    var name:string = "Rumone";
    # func sum(a:int, b:int):int -> {
    #     return a + b;
    # } 
    '''
)