/*1711790*/
grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::member {
def emit(self):
    tk = self.type
    if tk == UNCLOSE_STRING:       
        result = super.emit();
        raise UncloseString(result.text[1:]);
    elif tk == ILLEGAL_ESCAPE:
        result = super.emit();
        raise IllegalEscape(result.text);
    elif tk == ERROR_CHAR:
        result = super.emit();
        raise ErrorToken(result.text); 
    else:
        return super.emit();
}

options{
	language=Python3;
}

/*2. Program structure */
program : manyDecls EOF; 

manyDecls: decl manyDecls | decl ; 

decl: varDecl | funcDecl ;

/*2.1.Var Declaration*/
varDecl: primType var (COMMA var)* SEMI ;

var: ID | ID LS INTLIT RS ; //second also inArrPtrType

/*2.2. Function Declaration */
funcDecl: returnType ID LB paraList? RB blockStmt;

returnType: primType | outArrPtrType | VOID ; 

paraList: paraDecl COMMA paraList | paraDecl ;

paraDecl: primType ID | primType ID LS RS ;
/*block statement described later*/

/*7. Statements */
blockStmt: LP (blockMem)* RP ; 

blockMem: varDecl | stmt ;

stmt: ifStmt | dowhileStmt | forStmt | breakStmt | contStmt | returnStmt | expStmt | blockStmt ;

ifStmt: IF LB exp RB stmt (ELSE stmt)? ;

dowhileStmt: DO (stmt)+ WHILE exp SEMI ;

forStmt: FOR LB exp SEMI exp SEMI exp RB stmt ;

breakStmt: BREAK SEMI ;

contStmt: CONTINUE SEMI ;

returnStmt: RETURN exp? SEMI ;

expStmt: exp SEMI ;

/*6. Expressions */
exp : exp1 ASSIGN exp | exp1 ;
exp1: exp1 OR exp2 | exp2 ; 
exp2: exp2 AND exp3 | exp3 ;
exp3: exp4 EQ exp4 | exp4 NEQ exp4 | exp4 ;
exp4: exp5 LT exp5 | exp5 LEQ exp5 | exp5 GT exp5 | exp5 GEQ exp5 | exp5 ;
exp5: exp5 ADD exp6 | exp5 SUB exp6 | exp6 ;
exp6: exp6 DIV exp7 | exp6 MUL exp7 | exp6 MOD exp7 | exp7 ;
exp7: NOT exp7 | SUB exp7 | exp8 ;
exp8: exp9 LS exp RS | exp9 ;
exp9: LB exp RB | (INTLIT | FLOATLIT | BOOLEANLIT | STRINGLIT | ID | invokeExp) ;
invokeExp: ID LB (exp (COMMA exp)*)? RB ; 

/*4. Types Values */
inArrPtrType: primType ID LS RS ;
outArrPtrType: primType LS RS ;
primType:  INT | FLOAT | BOOLEAN | STRING ; 

/*3.1. Character Set (Last) */
WS: [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

/*3.2. Comment */
BLOCK_COMMENT: '/*' .*?  '*/' -> skip ;

LINE_COMMENT: '//' ~[\r\n]* -> skip ;

/*3.5. Literals*/
INTLIT: [0-9]+;

FLOATLIT : [0-9]+ '.' [0-9]* EXPONENT? | '.' [0-9]+ EXPONENT?|   [0-9]+ EXPONENT ; 

fragment EXPONENT : [eE]'-'?[0-9]+ ; 

BOOLEANLIT: TRUE | FALSE;

STRINGLIT: '"' (STRCHAR|ESCSEQ)* '"'
    {
        s = self.text[1:-1]
        self.text = s
    }
;
fragment STRCHAR: ~[\b\n\t\r\f"\\] ;
fragment ESCSEQ: '\\' [btnfr"\\] ;

/*3.3. Token Set */
/*Keywords*/
BOOLEAN: 'boolean' ;

BREAK: 'break' ;

CONTINUE: 'continue';

ELSE: 'else' ;

FOR: 'for' ;

FLOAT: 'float' ;

IF: 'if' ;

INT: 'int' ;

RETURN: 'return' ;

VOID: 'void' ;

DO: 'do' ;

WHILE: 'while' ;

TRUE: 'true' ;

FALSE: 'false' ;

STRING: 'string' ;
/*Operators*/
ADD: '+' ;

SUB: '-' ;

MUL: '*' ;

DIV: '/' ;

MOD: '%' ;

NOT: '!' ;

OR: '||' ;

AND: '&&' ;

EQ: '==' ;

NEQ: '!=' ;

LT: '<' ;

LEQ: '<=' ;

GT: '>' ;

GEQ: '>=' ;

ASSIGN: '=' ;
/*Identifiers*/
ID: [_a-zA-Z][_a-zA-Z0-9]* ;

/*3.4. Seperators*/
LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

LS: '[' ;

RS: ']' ;

SEMI: ';' ;

COMMA: ',' ;

ERROR_CHAR:.
    {
        raise ErrorToken(self.text)
    }
;

ILLEGAL_ESCAPE: '"' ('\\' [bfrnt"\\] | ~["\\])*? ([\\] ~[bfrnt"\\]) 
    {
        raise IllegalEscape(self.text[1:])
    }
;
UNCLOSE_STRING:  '"' ('\\' [bfrnt"\\] | ~[\b\f\r\n\t"\\])* (NL | EOF)
    {
        if self.text[-1]=='\n':
            raise UncloseString(self.text[1:-2])
        else:
            raise UncloseString(self.text[1:])
    }
;
NL: '\r'?'\n';