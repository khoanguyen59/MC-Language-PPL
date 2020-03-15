
"""
 * @author nhphung
"""
#Student ID: 1711790
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

class StaticChecker(BaseVisitor,Utils):

    global_envi = [
    Symbol("getInt",MType([],IntType())),
    Symbol("putInt",MType([IntType()],VoidType())),
    Symbol("putIntLn",MType([IntType()],VoidType())),
    Symbol("getFloat",MType([],FloatType())),
    Symbol("putFloat",MType([FloatType()],VoidType())),
    Symbol("putFloatLn",MType([FloatType()],VoidType())),
    Symbol("putBool",MType([BoolType()],VoidType())),
    Symbol("putBoolLn",MType([BoolType()],VoidType())),
    Symbol("putString",MType([StringType()],VoidType())),
    Symbol("putStringLn",MType([StringType()],VoidType())),
    Symbol("putLn",MType([],VoidType()))
    ]
     
    #List cac ham va bien toan cuc
    global_declaration = []
    list_func = []
    #List cac ham da duoc goi
    invoked_func = []
    
    def __init__(self,ast):
        #print(ast)
        #print(ast)
        #print()
        self.ast = ast

    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def checkNoEntryPoint(self, lstFunc):
        if self.lookup("main", lstFunc, lambda x: x.name) is None:
            raise NoEntryPoint()
            
    def visitProgram(self,ast, c): 
        #Clear the list after each program
        StaticChecker.global_declaration = []
        StaticChecker.list_func = []
        StaticChecker.invoked_func = ['main']
        for x in ast.decl:
            if type(x) is VarDecl:
                StaticChecker.global_declaration += [Symbol(x.variable, x.varType)]
            elif type(x) is FuncDecl:
                StaticChecker.global_declaration += [Symbol(x.name.name, MType([i.varType for i in x.param], x.returnType))]
                StaticChecker.list_func += [Symbol(x.name.name, MType([i.varType for i in x.param], x.returnType))]
        self.checkNoEntryPoint(StaticChecker.list_func)
        reduce(lambda x,y: x + [self.visit(y,x)], ast.decl, c)
        for x in StaticChecker.list_func:
            if self.lookup(x.name, StaticChecker.invoked_func, lambda y: y) is None:
                raise UnreachableFunction(x.name)

    def visitFuncDecl(self,ast, c): 
        t = ast.name.name
        if self.lookup(t, c, lambda x: x.name) is not None:
            raise Redeclared(Function(),t)
            
        try:
            local_param = reduce(lambda x,y: x + [self.visit(y,x)], ast.param, [])
        except Redeclared as e1: 
            raise Redeclared(Parameter(), e1.n)
        ldecl = list(filter(lambda x: type(x) is VarDecl, ast.body.member))
        local_varDecl = []
        isReturn = False;
        allStmt = []
        #ldecl_ID = list(filter(lambda x: x, ast.body.member))
        #if self.lookup(
        for x in ast.body.member:
            if type(x) is VarDecl and self.lookup(x.variable, local_varDecl + local_param, lambda y: y.name) is None:
                    local_varDecl += [Symbol(x.variable, x.varType)]
            elif type(x) is Return:
                if type(ast.returnType) is VoidType:
                    if x.expr is not None:
                        raise TypeMismatchInStatement(x)
                elif type(ast.returnType) is ArrayPointerType:
                    compareType = type(self.visit(x.expr, local_varDecl + local_param + c + [ast.name.name]))
                    if compareType is not ArrayPointerType and compareType is not ArrayType or type(self.visit(x.expr, local_varDecl + local_param + c + [ast.name.name]).eleType) is not type(ast.returnType.eleType):
                        raise TypeMismatchInStatement(x)
                else:
                    if type(ast.returnType) is not type(self.visit(x.expr, local_varDecl + local_param + c + [ast.name.name])):
                        raise TypeMismatchInStatement(x)
                isReturn = True;
            else:
                allStmt += [self.visit(x, (local_varDecl + local_param + c + [ast.returnType] + [ast.name.name]))]
        isChildReturn = self.lookup(True, list(filter(lambda x: type(x) == bool, allStmt)), lambda y: y)
        if type(ast.returnType) != VoidType and (isReturn == False and isChildReturn is None):
            raise FunctionNotReturn(t)
        return Symbol(t, MType([i.varType for i in ast.param], ast.returnType)) 
    
    def visitVarDecl(self, ast, c):
        if self.lookup(ast.variable, list(filter(lambda x: type(x) == Symbol, c)), lambda y: y.name) is not None:
            raise Redeclared(Variable(), ast.variable)
        return Symbol(ast.variable, ast.varType)
 
    def visitBlock(self, ast, c):
        local_varDecl = []
        allBlockStmt = []
        for x in ast.member:
            if type(x) is VarDecl and self.lookup(x.variable, local_varDecl, lambda y: y.name) is None:
                local_varDecl += [Symbol(x.variable, x.varType)]
             #   raise Redeclared(Variable(), ast.variable)
            #if type(x) is Id and self.lookup(x.name, c + local_varDecl + StaticChecker.global_declaration, lambda y: y.name) is None:
             #   raise Undeclared(Identifier(), x.name)
            #elif type(x) is CallExpr and self.lookup(x.method, c + local_varDecl, lambda y: y.name) is None:
                #raise Undeclared(Function(), x.method.name)
            else:
                allBlockStmt += [self.visit(x, local_varDecl + c)]
        if self.lookup(True, list(filter(lambda x: type(x) == bool, allBlockStmt)), lambda y: y) is True:        
            return True
        
    def visitIf(self, ast, c):
        if type(self.visit(ast.expr, c)) is not BoolType:
            raise TypeMismatchInStatement(ast)
        TS = self.visit(ast.thenStmt, c)
        if ast.elseStmt is None:
            return
        else:
            ES = self.visit(ast.elseStmt, c)
            if TS is True and ES is True:
                return True
            
    def visitFor(self, ast, c):
        if type(self.visit(ast.expr1, c)) is not IntType or type(self.visit(ast.expr2, c)) is not BoolType or type(self.visit(ast.expr3, c)) is not IntType:
            raise TypeMismatchInStatement(ast)
        isInForLoop = True;
        self.visit(ast.loop, c + [ast]) 
        return
        
    def visitDowhile(self, ast, c):
        if type(self.visit(ast.exp, c)) is not BoolType:
            raise TypeMismatchInStatement(ast)
        dowhileStmt = reduce(lambda x,y: x + [self.visit(y,x + [ast])], ast.sl, c)
        if self.lookup(True, list(filter(lambda x: type(x) is bool, dowhileStmt)), lambda y: y) is not None:
            return True
        
    def visitReturn(self, ast, c):
        if self.lookup(VoidType(), list(filter(lambda y: type(y) is VoidType, c)), lambda z: z) is not None:
            if ast.expr is not None:
                raise TypeMismatchInStatement(ast)
        elif self.lookup(ArrayPointerType, list(filter(lambda y: type(y) is ArrayPointerType, c)), lambda z: type(z)) is not None:
            if ast.expr is None:
                raise TypeMismatchInStatement(ast)
            compareType = type(self.visit(ast.expr, c))
            if compareType is not ArrayPointerType and compareType is not ArrayType or type(self.visit(ast.expr, c).eleType) is not type(self.lookup(ArrayPointerType, list(filter(lambda y: type(y) is ArrayPointerType, c)), lambda z: type(z)).eleType):
                raise TypeMismatchInStatement(ast)
        else:
            if ast.expr is None:
                raise TypeMismatchInStatement(ast)
            if list(filter(lambda y: type(y) is type(self.visit(ast.expr, c)), c)) == []:
                raise TypeMismatchInStatement(ast) 
        #if ast.expr is not None and type(ast.expr) is Id:
         #   self.lookup(ast.name, c + StaticChecker.global_declaration, lambda y: y.name)
        return True
    
    def visitBreak(self, ast, c):
        isInFor = self.lookup(For, list(filter(lambda x: type(x) == For, c)), lambda y: type(y))
        isInDowhile = self.lookup(Dowhile, list(filter(lambda x: type(x) == Dowhile, c)), lambda y: type(y))
        if isInFor is None and isInDowhile is None:
            raise BreakNotInLoop
            
    def visitContinue(self, ast, c):
        isInFor = self.lookup(For, list(filter(lambda x: type(x) == For, c)), lambda y: type(y))
        isInDowhile = self.lookup(Dowhile, list(filter(lambda x: type(x) == Dowhile, c)), lambda y: type(y))
        if isInFor is None and isInDowhile is None:
            raise ContinueNotInLoop
        
    def visitArrayCell(self, ast, c):
        if (type(self.visit(ast.arr, c)) is not ArrayType and type(self.visit(ast.arr, c)) is not ArrayPointerType) or type(self.visit(ast.idx, c)) is not IntType:
            raise TypeMismatchInExpression(ast)
        return self.visit(ast.arr, c).eleType
    
    def visitUnaryOp(self, ast, c):
        if ast.op == '-':
            lst = [IntType, FloatType]
            if type(self.visit(ast.body, c)) not in lst:
                raise TypeMismatchInExpression(ast)
        else:
            if type(self.visit(ast.body, c)) is not BoolType:
                raise TypeMismatchInExpression(ast)
        return self.visit(ast.body, c)
        
    def visitBinaryOp(self, ast, c):
        
        LHS = self.visit(ast.left, c)
        RHS = self.visit(ast.right, c)
        if ast.op == '=':
            assignLst = [IntType, FloatType, StringType, BoolType]
            if type(ast.left) is Id or (type(ast.left) is ArrayCell and (type(self.visit(ast.left.arr, c)) is ArrayPointerType or type(self.visit(ast.left.arr, c)) is ArrayType)):
                if type(LHS) not in assignLst:
                    raise TypeMismatchInExpression(ast)
                elif type(LHS) == type(RHS) or (type(LHS) is FloatType and type(RHS) is IntType):
                    return LHS
                else:
                    raise TypeMismatchInExpression(ast)
            else:
                raise NotLeftValue(ast.left)
        else:
            if type(LHS) == type(RHS):
                if type(LHS) is BoolType and ast.op in ['&&','||','==','!=']:
                    return BoolType()
                elif type(LHS) is IntType:
                    if ast.op in ['+', '-', '*', '%', '/']:
                        return IntType()
                    elif ast.op in ['<', '<=', '>', '>=', '==', '!=']:
                        return BoolType()
                    #elif ast.op == '/':
                        #return FloatType()
                elif type(LHS) is FloatType:
                    if ast.op in ['+', '-', '*', '/']:
                        return FloatType()
                    elif ast.op in ['<', '<=', '>', '>=']:
                        return BoolType()
                raise TypeMismatchInExpression(ast)
            else:
                lst = [IntType, FloatType]
                if type(LHS) in lst and type(RHS) in lst:
                    if ast.op in ['+', '-', '*', '/']:
                        return FloatType()
                    elif ast.op in ['<', '<=', '>', '>=', '==', '!=']:
                        return BoolType()
                raise TypeMismatchInExpression(ast)
            
    def visitCallExpr(self, ast, c): 
        res = self.lookup(ast.method.name, list(filter(lambda x: type(x) == Symbol, c + StaticChecker.global_declaration)), lambda y: y.name)
        isRecursive = self.lookup(ast.method.name, list(filter(lambda x: type(x) == str, c)), lambda y: y)
        isInvoked = self.lookup(ast.method.name, list(filter(lambda x: type(x) == str, StaticChecker.invoked_func)), lambda y: y)
        if res is not None and isRecursive is None and isInvoked is None:
            StaticChecker.invoked_func += [ast.method.name]
        if res is None:
            raise Undeclared(Function(),ast.method.name)
        if type(res.mtype) is not MType:
            raise TypeMismatchInExpression(ast)
        paramLst = [self.visit(x,c) for x in ast.param]
        if len(res.mtype.partype) != len(paramLst):
            raise TypeMismatchInExpression(ast)
        else:
            if all(((type(x) == type(y) and type(x) is not ArrayPointerType) or ((type(x) == ArrayType or type(x) == ArrayPointerType) and type(y) == ArrayPointerType and type(x.eleType) == type(y.eleType))) for (x,y) in zip(paramLst, res.mtype.partype)) is True:
                pass
            else:
                raise TypeMismatchInExpression(ast)
        return res.mtype.rettype

    def visitIntLiteral(self,ast, c): 
        return IntType()
    
    def visitFloatLiteral(self, ast, c):
        return FloatType()
        
    def visitBooleanLiteral(self, ast, c):
        return BoolType()
        
    def visitStringLiteral(self, ast, c):
        return StringType()

    def visitId(self, ast, c):
        res = self.lookup(ast.name, list(filter(lambda x: type(x) == Symbol, c + StaticChecker.global_declaration)), lambda y: y.name)
        res_func = self.lookup(ast.name, StaticChecker.list_func, lambda x: x.name)
        #if res is None or (res_func is not None):
        if res is None:
            raise Undeclared(Identifier(), ast.name)
        return res.mtype
