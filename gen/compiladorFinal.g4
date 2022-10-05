grammar compiladorFinal;

prog
    : decVars* decFunctions* blockMain
    ;

blockMain
    : DEF MAIN '()' '{' block '}'
    ;

block
    : func_for block
    | func_break block
    | func_do_while block
    | func_if (func_else)? block
    | func_print block
    | assigment block
    | function_call ';' block
    | func_return block
    | decVars block
    |
    ;

blockVoid
    : func_for blockVoid
    | func_break blockVoid
    | func_do_while blockVoid
    | func_if (func_else)? blockVoid
    | func_print blockVoid
    | assigment blockVoid
    | function_call ';' blockVoid
    | decVars block
    |
    ;

decVars
    : TYPE ID ('=' expr)? (',' ID ('=' expr)?)* ';'
    ;

decFunctions
    : DEF ID '(' (TYPE ID (',' TYPE ID)*)? ')' TYPE '{' block '}'
    | DEF ID '(' (TYPE ID (',' TYPE ID)*)? ')' VOID '{' blockVoid '}'
    ;

func_return
    : RETURN (expr)? ';'
    ;

// For each
func_for returns [idx]
    : FOR ID IN RANGE '(' expr ':' expr (':' expr)? ')' '{' block '}'
    ;

//do_while
func_do_while
    : DO '{' block '}' WHILE expr ';'
    ;

func_break
    : BREAK ';'
    ;

// if
func_if
    : IF expr '{' block '}'
    ;

func_else
    : ELSE '{' block '}'
    ;

// print
func_print
    : PRINT (expr (',' expr)*)? ';'
    ;

function_call returns [type]
    : ID '(' (expr (',' expr)*)? ')'
    ;

assigment
    : ID '=' expr ';'
    | ID '=' INPUT '()' ';'
    ;

expr returns [type, inh_type]
    : expr OR term
    | term
    ;

term returns [type]
    : term AND term2
    | term2
    ;

term2 returns [type]
    : term2 op=('>' | '<' | '<=' | '>=') term3
    | term3
    ;

term3 returns [type]
    : term3 op=('==' | '!=') term4
    | term4
    ;

term4 returns [type]
    : term4 op=('+' | '-') term5
    | term5
    ;

term5 returns [type]
    : term5 op=('*' | '/') term6
    | term6
    ;

term6 returns [type]
    : op=('-' | NOT) term6
    | factor
    ;

factor  returns [type]
    : '(' expr ')'
    | function_call
    | ID
    | INT_VALUE
    | FLOAT_VALUE
    | STR_VALUE
    | BOOL_VALUE
    ;

// P.R.
//Operadores lógicos
OR: 'or';
AND: 'and';
NOT: 'not';

//Comandos
FOR: 'for';
BREAK: 'break';
IF: 'if';
ELSE: 'else';
DO: 'do';
WHILE: 'while';
IN: 'in';
DEF: 'def';
MAIN: 'main';
RETURN: 'return';

//tipos
VOID: 'void';
TYPE: 'int'
    | 'float'
    | 'string'
    | 'boolean';

//Funções
PRINT: 'print';
INPUT: 'input';
RANGE: 'range';

//Valores
INT_VALUE: [0-9]+;
FLOAT_VALUE: [0-9]+[.][0-9]+;
STR_VALUE: ["]~["]*["];
BOOL_VALUE: 'True' | 'False';

//ID
ID: [a-zA-Z][a-zA-Z0-9]*;
WS: [ \t\r\n] -> skip;
