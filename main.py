from uwu_parser import UWUParser
from uwu_lexer import UWULexer
from uwu_global import UWU_GLOBAL
from codegen import CodeGen

def main():
    fname = "input.uwu"
    with open(fname) as f:
        text_input = f.read()
        
    codegen = CodeGen()

    module = codegen.module
    builder = codegen.builder
    printf = codegen.printf

    pg = UWUParser(module, builder, printf)
    pg.parse(text_input)

    codegen.create_ir()
    codegen.save_ir("output.ll")

main()


