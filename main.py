from uwu_parser import UWUParser
from uwu_global import UWU_GLOBAL

def main():
    parser = UWUParser()
    # code_input = '''
    # a = 1
    # b = 2
    # c = 4 - 4
    # 1 + 3 
    # '''

    # tree = parser.parse(code_input)
    # print(tree)
    # print(tree.evaluate_node())
    # print(UWU_GLOBAL)
    while True:
        try:
            s = input('(^.^) >> ')
        except EOFError:
            break
        except KeyboardInterrupt:
            break
        tree = parser.parse(s, dbg=False)
        result = tree.evaluate_node()
        print(UWU_GLOBAL)


main()


