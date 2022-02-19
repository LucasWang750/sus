from ply import lex, yacc

tokens = ["PLUS", "MINUS", "ADD", "SUBTRACT"]

t_PLUS = r'\+'

def t_error(t):
    print(f"Illegal character {t.value[0]!r}")
    t.lexer.skip(1)