import mytokens
import ply.lex as lex
import ply.yacc as yacc
import re
start = 'exp'

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


def p_exp_start(p):
    'exp : stmnts exp'
    p[0]=p[1]+ p[2]


def p_exp_empty(p):
    'exp : '
    p[0] = []

def p_exp_stmnts(p):
    'stmnts : stmnt stmnts'
    p[0] = [p[1]] + p[2]
    

# def p_stmnt_stmnt(p):
#     'stmnt : stmnt stmnt'
#     p[0]=p[1]

def p_stmnt_empty(p):
    'stmnts : '
    p[0] = []
    
def p_exp_assign(p):
    'stmnt : IDENTIFIER EQUAL val'
    p[0] = ("assign", p[1],p[3])

def p_exp_puts(p):
    'stmnt : PUTS val'
    p[0] = ("puts",p[2])

def p_exp_array(p):
    'stmnt : IDENTIFIER EQUAL LEFTBRACKET vals RIGHTBRACKET'
    p[0] = ("array", p[1], p[4] )

def p_exp_nums(p):
    'vals : arrvals'
    p[0] = p[1]
    
def p_exp_num(p):
    'vals : '
    p[0] = []

def p_exp_valus(p):
    'arrvals : val COMMA arrvals'
    p[0] = [p[1]]+ p[3]
    
def p_exp_arrval(p):
    'arrvals : val'
    p[0]=[p[1]]

def p_exp_iter(p):
    'stmnt : ARRAYEACH DO LOOPVAR stmnts END'
    p[0]=("arrayeach",p[1],p[3],p[4])

def p_exp_for(p):
    'stmnt : FOR IDENTIFIER IN NUMBER DOTS NUMBER stmnts END'
    p[0]=("for",p[4],p[6],p[7])
    
def p_exp_val_num(p):
    'val : NUMBER'
    p[0] = ("number", p[1])


def p_exp_val_str(p):
    'val : STRING'
    p[0] = ("string",p[1])
    
def p_exp_val_id(p):
    'val : IDENTIFIER'
    p[0] = ("var",p[1])

def p_exp_val_op(p):
    'val : val OPERATOR val'
    p[0]=("binop", p[1],p[2],p[3])

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

def fileread():
        with open('rubycode2.txt', 'r') as f:
             read_data = f.read()
        f.closed
        return read_data

def update_env(environment, var, val):
    environment[var]=val
    
def env_lookup(environment, var):
    if var in environment:
        return environment[var]
    else:
        return None

def eval_exp(environment, tree):
    nodetype = tree[0]

    if nodetype == "number":
        return int(tree[1])
    elif nodetype == "string":
        return tree[1]
    elif nodetype == "var":
        return env_lookup(environment, tree[1])
    elif nodetype == "assign":
        var=tree[1]
        val=eval_exp(environment,tree[2])
        update_env(environment,var,val)
    
    elif nodetype == "array":
        temp=[]
        treelen=len(tree[2])
        lvar=0
        
        while lvar!=treelen:
            temp.append( eval_exp(environment, tree[2][lvar]) )
            
            lvar=lvar+1
        # print temp
        update_env(environment, tree[1], temp)
    elif nodetype == "arrayeach":
        # print tree[1]
        temp=re.search( '[A-Za-z][A-Za-z_]*',tree[1]).group(0)
        # print temp
        arrayvalues = env_lookup(environment, temp)
        times=0
        # while time!=len(arrayvalues):
            
        
    elif nodetype == "binop":
        left_child = tree[1]
        operator = tree[2]
        right_child = tree[3]
        left_val = eval_exp(environment, left_child)
        right_val = eval_exp(environment, right_child)
        if operator == "+":
            return left_val + right_val
        elif operator == "-":
            return left_val - right_val
        elif operator == "*":
            return left_val * right_val
        elif operator == "/":
            return left_val / right_val
    elif nodetype =="puts":
        x=tree[1]
        # print tree[0]
        # print x
        print eval_exp(environment, x)

            # elif tree[1] 
# here's some code to test with
rubylexer = lex.lex(module=mytokens)
rubyparser = yacc.yacc()
data=fileread()
rubyast = rubyparser.parse(data)
print rubyast


environment = {}
loopvar=0
while loopvar!=len(rubyast):

    eval_exp(environment, rubyast[loopvar])
    loopvar=loopvar+1
