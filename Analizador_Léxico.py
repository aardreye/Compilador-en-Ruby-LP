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
