import autoprojtokens
#import jsgrammar
import ply.lex as lex
import ply.yacc as yacc

start = 'exp'

precedence = (
    
        ('left', 'NUMBER'),
        # ('left', 'ANDAND'),
        # ('left', 'EQUALEQUAL'),
        # ('left', 'LT', 'LE', 'GT', 'GE'),
        # ('left', 'PLUS', 'MINUS'),
        # ('left', 'TIMES', 'DIVIDE'),
        # ('right', 'NOT'),
)

tokens = (
        'NEWLINE',
        'TAB',
        'SPACE',
        # 'ASSIGNMENT',
        'ARRAYEACH',
        'DO',
        'LOOPVAR',
        'PUTS',
        'END',
        'IDENTIFIER',
        'NUMBER',
        'OPERATOR',
        'LEFTBRACKET',
        'RIGHTBRACKET',
)



def p_exp_call(p):
    'exp : NUMBER'
    p[0] = ("call", p[1])

# def p_exp_number(p):
#     'exp : number'
#     p[0] = ("number", p[1])

# def p_optargs(p):
#     'optargs : args'
#     p[0] = p[1] # the work happens in "args"


def p_error(p):
    print "Syntax error in input!"

# here's some code to test with
rubylexer = lex.lex(module=autoprojtokens)
rubyparser = yacc.yacc()
rubyast = rubyparser.parse("71", lexer=rubylexer)
print rubyast
