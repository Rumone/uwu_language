from uwu_parser import UWUParser
from uwu_global import UWU_GLOBAL
from codegen import CodeGen

def main():
    parser = UWUParser()
    
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


main()


