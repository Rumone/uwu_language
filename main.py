from uwu_parser import UWUParser
from uwu_global import UWU_GLOBAL

def main():
    parser = UWUParser()
    
    code_input = '''
    () -> {
        test = 3
        foo = 3
        bar = 3
        b = 2

        x = 2 is 2

        func foobar () -> {
            c = bar + 5
        }

        foobar()
    }
    '''

    tree = parser.parse(code_input)
    tree.evaluate_node()
    # print(tree)
    print(UWU_GLOBAL)
    
    
    # while True:
    #     try:
    #         s = input('(^.^) >> ')
    #     except EOFError:
    #         break
    #     except KeyboardInterrupt:
    #         break
    #     tree = parser.parse(s, dbg=True)
    #     result = tree.evaluate_node()
    #     print(tree)
    #     print(UWU_GLOBAL)


main()


