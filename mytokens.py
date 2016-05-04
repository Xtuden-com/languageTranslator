# This is a tokenizer of the automata project. I have covered iterator and for loop. 
# I have used many tokens and conditions like floating numbers, possible statement positions
# assignment statements of string, identifier or another variable
import ply.lex as lex

tokens = (
        
        'NEWLINE',
        'TAB',
        'SPACE',
        # 'ASSIGNMENT',
        'ARRAYEACH',
        'FOR',
        'IN',
        'DOTS',
        'DO',
        'LOOPVAR',
        'PUTS',
        'END',
        'STRING',
        'COMMA',
        'IDENTIFIER',
        'NUMBER',
        'EQUAL',
        'OPERATOR',
        'LEFTBRACKET',
        'RIGHTBRACKET',
)


def t_DOTS(t):
        r'\.\.'
        return t
        

t_ignore = ' \t\v\r' # whitespace

# def t_newline(t):
#         r'\n'
#         t.lexer.lineno += 1

# def t_error(t):
#         print "JavaScript Lexer: Illegal character " + t.value[0]
#         t.lexer.skip(1)


# def t_IDENTIFIER(token):
#         r'[A-Za-z][A-Za-z_]*'
        # return token
# def t_NUMBER(token):
#         r'-?[0-9]+(?:\.[0-9]*)?'
#         # token.value = float(token.value)
#         return token
# def t_STRING(token):
#         r'"(?:[^?\\]|(?:\\.))*"'
#         token.value = token.value[1:-1]
#         return token



def t_NEWLINE(t):
        r'\n'
 
def t_TAB(t):
        r'\s\s\s\s'
        return t

def t_SPACE(t):
        r'\s'
        return t
        
        
def t_ARRAYEACH(t):
        r'[A-Za-z][A-Za-z_]*\.each'
        return t
        
def t_FOR(t):
        r'for'
        return t
def t_IN(t):
        r'in'
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
        
def t_STRING(t):
        r'"[^"]*"'
        # r'"["]*"'
        t.value = t.value[1:-1] # drop "surrounding quotes"
        return t
        
# def t_LISTITEM(t):
#         r'[0-9]+[,]?'
        
#         # if t.value[-1]==',':
#         # t.value=t.value[1,-1]
#         return t
        
        # return t

def t_COMMA(t):
        r','
        return t
        
def t_IDENTIFIER(t):
        r'[A-Za-z][A-Za-z_]*'
        return t
        
def t_NUMBER(t):
        r'-?[0-9]+(?:\.[0-9]+)?'
        t.value = float(t.value)

        return t
        
def t_EQUAL(t):
        r'='
        return t
        
def t_OPERATOR(t):
        r'[<|>|==|!=|+|-]'
        return t

def t_LEFTBRACKET(t):
        r'\['
        return t

def t_RIGHTBRACKET(t):
        r'\]'
        return t

def t_error(t):
        pass


def fileread():
        with open('rubycode.txt', 'r') as f:
             read_data = f.read()
        f.closed
        return read_data
        
def main():
        # text = " i = 13  2 3abc\n \t"
        text=fileread()
        print text
        rubylex = lex.lex()
        rubylex.input(text)
        while True:
                tok = rubylex.token()
                if not tok: break
                print tok
                

if __name__ == "__main__":
        main()
        