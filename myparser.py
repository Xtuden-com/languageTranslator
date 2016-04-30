import mytokens
import ply.lex as lex
import ply.yacc as yacc

start = 'exp'

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
        'LISTITEM',
        'IDENTIFIER',
        'NUMBER',
        'OPERATOR',
        'LEFTBRACKET',
        'RIGHTBRACKET',
)

def p_exp_call(p):
    'exp : IDENTIFIER OPERATOR NUMBER'
    p[0] = ("assign", p[1],p[3])

# def p_exp_number(p):
#     'exp : NUMBER'
#     p[0] = ("number", p[1])

# def p_optargs(p):
#     'optargs : args'
#     p[0] = p[1] # the work happens in "args"

# def p_optargsempty(p):
#     'optargs : '
#     p[0] = [] # no arguments -> return the empy list

# def p_args(p):
#     'args : exp COMMA args'
#     p[0] = [p[1]] + p[3]

# def p_args_last(p): # one argument
#     'args : exp'
#     p[0] = [p[1]]

def p_error(p):
    print "Syntax error in input!"

# here's some code to test with
rubylexer = lex.lex(module=mytokens)
rubyparser = yacc.yacc()
rubyast = rubyparser.parse("i=11")
print rubyast
