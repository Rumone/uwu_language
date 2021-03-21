from lexer import Lexer
from parser import Parser
from codegen import CodeGen

fname = "input.uwu"
with open(fname) as f:
    text_input = f.read()

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

codegen = CodeGen()

module = codegen.module
builder = codegen.builder
printf = codegen.printf

pg = Parser(module, builder, printf)
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()

codegen.create_ir()
codegen.save_ir("output.ll")




    # code_input = '''
    # () -> {
    #     print["I am great"]
    # }
    # '''

    # tree = parser.parse(code_input, dbg=True)
    # tree.evaluate_node()
    # # print(tree)
    # print(UWU_GLOBAL)
    
    
    while True:
        try:
            s = input('(^.^) >> ')
        except EOFError:
            break
        except KeyboardInterrupt:
            break
        tree = parser.parse('() -> {' + s + '}', dbg=False)
        result = tree.evaluate_node()
        # print(tree)
        print(UWU_GLOBAL)