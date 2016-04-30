# import lex
import ply.lex as lex
import ply.yacc as yacc

# import lex

tokens = (
        # 'space',
        # 'TAB',
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

#t_ignore                = ' \t\v\r' # shortcut for whitespace

# def t_STRING(t):
#         r'"[^"]*"'
#         t.value = t.value[1:-1] # drop "surrounding quotes"
#         return t

# the line below can be commented to detect white spaces
t_ignore                = ' \t\v\r\n' # shortcut for whitespace


def t_NEWLINE(t):
        r'\n'
 
        
def t_TAB(t):
        r'\s\s\s\s'
        return t

def t_SPACE(t):
        r'\s'
        return t
        
        
# def t_assignment(t):
#         r'[A-Za-z][A-Za-z_]*\s=\s[0-9]+'
#         return t
        
def t_ARRAYEACH(t):
        r'[A-Za-z][A-Za-z_]*\.each'
        return t
def t_DO(t):
        r'do'
        return t
def t_LOOPVAR(t):
        r'\|[A-Za-z][A-Za-z_]*\|'
        return t
def t_PUTS(t):
        r'puts'
        return t
def t_END(t):
        r'end'
        return t        
        
       
        # return t
        
        
def t_IDENTIFIER(t):
        r'[A-Za-z][A-Za-z_]*'
        return t
        
        
def t_NUMBER(t):
        r'[0-9]+'
        return t
        
def t_OPERATOR(t):
        r'[<|>|==|=|!=|+|-]'
        return t
        

        
# def t_braces(t):
#         # r'{[^{}]*}'
#         # r'"["]*"'
#         r'{[^{]*}'
#         t.value = t.value[1:-1] # drop "surrounding quotes"
#         return t
def t_LEFTBRACKET(t):
        r'\['
        return t
def t_RIGHTBRACKET(t):
        r'\]'
        return t
def t_error(t):
        pass

# def t_EQUAL(t):
#         r'='
#         return t
# def t_STRING(t):
#         r'"[^"]*"'
#         # r'"["]*"'
#         t.value = t.value[1:-1] # drop "surrounding quotes"
#         return t
# def t_WORD(t):
#         r'[^ <>\n]+'
#         return t
# text = "Hello \t<b>World</c>"

#########################################################
#########################################################
#########################################################


# def fileread():
#         # print 2
#         with open('rubycode.txt', 'r') as f:
#              read_data = f.read()
#         f.closed
#         return read_data
        
# def main():
#         # text = " i = 13  2 3abc\n \t"
#         text=fileread()
#         print text
#         rubylex = lex.lex()
#         rubylex.input(text)
#         while True:
#                 tok = rubylex.token()
#                 if not tok: break
#                 print tok
                
                
#         # rubyparser=yacc.yacc()
#         # rubyast=rubyparser.parse("i=1",lexer=rubylex);
#         # print rubyast
# if __name__ == "__main__":
#         main()
        