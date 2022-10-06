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
    : DEF ID '(' (TYPE ID (',' TYPE ID)*)? ')' TYPE '{' block '}'       #func_type
    | DEF ID '(' (TYPE ID (',' TYPE ID)*)? ')' VOID '{' blockVoid '}'   #func_void
    ;

func_return
    : RETURN (expr)? ';'
    ;

// For
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
    : ID '=' expr ';'       #assigment_expr
    | ID '=' INPUT '()' ';' #assigment_input
    ;

expr returns [type, inh_type]
    : expr OR term  #operation_or
    | term          #go_term
    ;

term returns [type]
    : term AND term2    #operation_and
    | term2             #go_term2
    ;

term2 returns [type]
    : term2 op=('>' | '<' | '<=' | '>=') term3  #operation_comparation
    | term3                                     #go_term3
    ;

term3 returns [type]
    : term3 op=('==' | '!=') term4  #operation_equal_dif
    | term4                         #go_term4
    ;

term4 returns [type]
    : term4 op=('+' | '-') term5    #operation_plus_sub
    | term5                         #go_term5
    ;

term5 returns [type]
    : term5 op=('*' | '/') term6    #operation_multi_div
    | term6                         #go_term6
    ;

term6 returns [type]
    : op=('-' | NOT) term6  #operation_minus_not
    | factor                #go_factor
    ;

factor  returns [type]
    : '(' expr ')'   #terminal_openClose_expr
    | ID             #terminal_id
    | INT            #terminal_int
    | FLOAT          #terminal_float
    | STRING         #terminal_string
    | BOOLEAN        #terminal_boolean
    | function_call  #terminal_function_call
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
INT: [0-9]+;
FLOAT: [0-9]+[.][0-9]+;
STRING: ["]~["]*["];
BOOLEAN: 'True' | 'False';

//ID
ID: [a-zA-Z][a-zA-Z0-9]*;
WS: [ \t\r\n] -> skip;
