grammar trabFinal;

prog
    :   decVars* decFunctions* blocoMain
    ;

decVars
    :   tipo (listaIds|listaAtribs) ';'
    |   (listaIds|listaAtribs) ';'//REMOVER
    ;
tipo
    :   'int'
    |   'real'
    |   'boolean'
    |   'string'//s maiusculo
    // | 'void'
    ;

listaIds
    :   ID (',' ID)*
    ;

listaAtribs
    :   (ID '=' NUMERO (',' ID '=' NUMERO )*)
    |   ID '=' ('"' (ID|NUMERO) '"')+//adicionar sinais
    |   ID '=' ('True'|'False')
    |   ID '=' ((ID|NUMERO) (op=('+'|'-'|'*'|'/') (ID|NUMERO))+)
    //|   ID '=' ((ID|NUMERO) (op=('+'|'-'|'*'|'/') (ID|NUMERO))+) fazer pra condicionais;
    ;

decFunctions
    :   'def' ID '(' tipo ID ')' tipo '{' expr '}' // return/break?
    |   blocoMain//ajustar o erro do bloco main
    ;//varios parametros

expr
    :   decVars
    |   decFunctions
    |   conditional
    |   print
    |   input
    |   repeat
    ;
//chamada de bloco de comandos não expressão
conditional
    :   'if' '(' logic ')' '{' expr '}' ('else' '{' expr '}')?
    ;//remover expr e colocar o bloco de comandos

logic
    :   logic op=('OR'|'||') logic2
    |   logic2
    ;
//atentar a gramatica, remover o or e o and
logic2
    :   logic2 op=('AND'|'&&') logic3
    |   logic3
    ;

logic3
    :   logic3 op=('>' | '<' | '>=' | '<=') logic4
    |   logic4
    ;
//concatenar com or ou and
logic4
    :   logic4 op=('==' | '!=') logic5
    |   logic5
    ;

logic5
    :   logic5 op=('+' | '-') logic6
    |   logic6
    ;

logic6
    :   logic6 op=('*' | '/') logic7
    |   logic7
    ;

logic7
    :   op=('-' | '!') logic7
    ;

//definir os terminais

print: 'print' '(' (ID|NUMERO) ')'
    ;
//expressoes
input:
    ;

// for e do while
// repeat
//     : 'for' ID 'in range' '(' (ID) ':' (ID) ')' ':'
//     ;

repeat
    :
    ;


blocoMain
    : 'def' 'main' '(' ')' '{' expr '}'
    ;
//bloco de comandos

NUMERO: [-]?[0-9]+('.'[0-9]+)?
    ;
//tratar o negativo no - unário
ID: [a-zA-Z][a-zA-Z0-9]*
    ;
WS: [ \t\r\n]+ -> skip;
