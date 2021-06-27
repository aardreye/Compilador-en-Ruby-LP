import ply.lex as lex

# AQUÍ EMPIEZA UNA PARTE DE MI TRABAJO - AARÓN REYES
# Mapa de palabras reservadas
reserved = {
    'and' : 'AND',
    'begin' : 'BEGIN',
    'break' : 'BREAK',
    'case' : 'CASE',
    'class' : 'CLASS',
    'def' : 'DEF',
    'do' : 'DO',
    'else' : 'ELSE',
    'elsif' : 'ELIF',
    'end' : 'END',
    'ensure' : 'ENSURE',
    'false' : 'FALSE',
    'true' : 'TRUE',
    'for' : 'FOR',
    'if' : 'IF',
    'in' : 'IN',
    'nil' : 'NIL',
    'not' : 'NOT',
    'or' : 'OR',
    'puts' : 'PUTS',
    'rescue' : 'RESCUE',
    'retry' : 'RETRY',
    'return' : 'RETURN',
    'then' : 'THEN',
    'unless' : 'UNLESS',
    'until' : 'UNTIL',
    'when' : 'WHEN',
    'while' : 'WHILE',
}
# Tupla de tokens
tokens = (
    'AND_LOGIC',
    'COINCIDENCE',
    'COMPOSITION',
    'DIVIDE',
    'EQUAL',
    'EQUALITY',
    'EQUALITY_OF_CASE',
    'EXPONENT',
    'GREATER_EQUAL',
    'GREATER_THAN',
    'L_PAREN',
    'MINUS',
    'MODULE',
    'MULTIPLICATION',
    'NEGATION',
    'NUMBER',
    'OR_LOGIC',
    'PLUS',
    'R_PAREN',
    'SMALLER_THAN',
    'SMALLER_EQUAL',
    'QUOTATION_MARK',
    'WRENCH_L',
    'WRENCH_R',
    'COMMA',
    'DOUBLE_QUOTE',
    'VARIABLE_LOCAL',
    'VARIABLE_INSTANCE',
    'VARIABLE_CLASS',
    'VARIABLE_GLOBAL',
    'CONSTANT'
) + tuple(reserved.values())
# AQUÍ TERMINA UNA PARTE DE MI TRABAJO - AARÓN REYES

# AQUÍ EMPIEZA UNA PARTE DE MI TRABAJO - AARÓN REYES
# Regla de expresiones regulares para los tokens
t_AND_LOGIC = r'&'
t_DIVIDE = r'/'
t_EQUALITY = r'=='
t_EQUALITY_OF_CASE = r'==='
t_EXPONENT = r'\*\*'
t_GREATER_EQUAL = r'>='
t_GREATER_THAN = r'>'
t_MINUS = r'-'
t_MODULE = r'%'
t_MULTIPLICATION = r'\*'
t_OR_LOGIC = r'\|'
t_PLUS = r'\+'
t_SMALLER_THAN = r'<'
t_SMALLER_EQUAL = r'<='
#################################################
t_COINCIDENCE = r'=~'
t_COMPOSITION = r'\|&'
t_EQUAL = r'\='
t_L_PAREN = r'\('
t_NEGATION = r'!'
t_R_PAREN = r'\)'
t_QUOTATION_MARK = r'\''
t_WRENCH_L = r'\{'
t_WRENCH_R = r'\}'
t_COMMA = r'\,'
t_DOUBLE_QUOTE = r'"'
t_ignore = ' \t'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
# AQUÍ TERMINA UNA PARTE DE MI TRABAJO - AARÓN REYES