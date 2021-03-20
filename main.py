from uwu_parser import UWUParser
from uwu_global import UWU_GLOBAL

def main():
    parser = UWUParser()
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


