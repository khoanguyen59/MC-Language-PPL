'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
#Nguyen Tran Phuong Khoa - 1711790
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                    Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("getFloat",MType([],FloatType()), CName(self.libName)),
                    Symbol("putFloat",MType([FloatType()],VoidType()), CName(self.libName)),
                    Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("putBool",MType([BoolType()],VoidType()), CName(self.libName)),
                    Symbol("putBoolLn",MType([BoolType()],VoidType()), CName(self.libName)),
                    Symbol("putString",MType([StringType()],VoidType()), CName(self.libName)),
                    Symbol("putStringLn",MType([StringType()],VoidType()), CName(self.libName)),
                    Symbol("putLn",MType([],VoidType()), CName(self.libName))
                ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

class ClassType(Type):
    def __init__(self, cname):
        #cname: String
        self.cname = cname

    def __str__(self):
        return "ClassType"

    def accept(self, v, param):
        return v.visitClassType(self, param)

class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MCClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = SubBody(None, self.env)
        for x in ast.decl:
            e = self.visit(x, e)
            
        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), None, Block(list())), c, Frame("<init>", VoidType))
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame

        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else list()
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        listParamArray = [] # list(Symbol(name, mtype, value: Index(idx)))
        listLocalArray = [] # list(Symbol(name, mtype, value: Index(idx)))
        
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        elif isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            e = SubBody(frame, glenv)
            for x in consdecl.param:
                e = self.visit(x, e)
                glenv = e.sym
                if type(x.varType) is ArrayType:
                    idx = glenv[0].value.value
                    self.emit.printout(self.emit.emitINITARRAY(idx, x.varType, frame))
                    listParamArray.append(glenv[0])
        
        for x in listParamArray:
            self.emit.printout(self.emit.emitCOPYARRAY(x.value.value, x.mtype, frame))
            
        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        
        # Generate code for statements
        if isInit:
        
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        #list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.member))
        for x in body.member:
            if type(x) is VarDecl:
                e = SubBody(frame, glenv)
                e = self.visit(x, e)
                glenv = e.sym
                if type(x.varType) is ArrayType:
                        idx = glenv[0].value.value
                        self.emit.printout(self.emit.emitINITARRAY(idx, x.varType, frame))
             #   self.emit.printout(self.visit(x, SubBody(frame, glenv))[0])
            else: 
                self.visit(x, SubBody(frame, glenv))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope();

    def visitFuncDecl(self, ast, o):
        #ast: FuncDecl
        #o: Any

        subctxt = o
        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, subctxt.sym, frame)
        return SubBody(None, [Symbol(ast.name.name, MType(list(), ast.returnType), CName(self.className))] + subctxt.sym)
    
    def visitBlock(self, ast, o):
        #ast: Block
        
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        for x in ast.member:
            self.visit(x, o)
        
    def visitVarDecl(self, ast, o):
        #ast: VarDecl
        #o: SubBody
        #ast.variable: Id
        #ast.varType: Type
        
        subctxt = o
        frame = subctxt.frame
        mtype = ast.varType
        name = ast.variable
        if frame is None:
            # Decl mot bien global
            self.emit.printout(self.emit.emitATTRIBUTE(name, mtype, False, ""))
            
            return SubBody(None, [Symbol(name, mtype, CName(self.className))] + subctxt.sym)
        else:
            # Decl mot bien local hoac param
            idx = frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(idx, name, mtype, frame.getStartLabel(), frame.getEndLabel(), frame))
            return SubBody(frame, [Symbol(name, mtype, Index(idx))] + subctxt.sym)
    
    def visitIf(self, ast, o):
        #ast: If
        #o: Any
        #expr:Expr
        #thenStmt:Stmt
        #elseStmt:Stmt
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        
        expr,_ = self.visit(ast.expr, Access(frame, nenv, False, True))
        self.emit.printout(expr)
        
        label1 = frame.getNewLabel()
        label2 = None
        if ast.elseStmt is not None:
            label2 = frame.getNewLabel()
            
        self.emit.printout(self.emit.emitIFFALSE(label1, frame))
        self.visit(ast.thenStmt, o)
        if ast.elseStmt is not None:
            self.emit.printout(self.emit.emitGOTO(str(label2), frame))
        self.emit.printout(self.emit.emitLABEL(label1,frame))
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, o)
            self.emit.printout(self.emit.emitLABEL(label2, frame))
        
    def visitDowhile(self, ast, o):
        #o: Any
        #ast.sl: List[Stmt]
        #ast.exp: Expr

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        
        frame.enterLoop()
        
        labelContinue = frame.getContinueLabel()
        labelBreak = frame.getBreakLabel()
        list(map(lambda x: self.visit(x, o), ast.sl))
        self.emit.printout(self.emit.emitLABEL(labelContinue,frame))
        
        expr, _ = self.visit(ast.exp, Access(frame, nenv, False, True))
        self.emit.printout(expr)
        self.emit.printout(self.emit.emitIFFALSE(labelBreak, frame))
        list(map(lambda x: self.visit(x, o), ast.sl))

        self.emit.printout(self.emit.emitGOTO(str(labelContinue), frame))
        self.emit.printout(self.emit.emitLABEL(labelBreak,frame))
        
    def visitFor(self, ast, o):
        #o: Any
        #expr1:Expr
        #expr2:Expr
        #expr3:Expr
        #loop:Stmt
        
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        
        expr1, _ = self.visit(ast.expr1, Access(frame, nenv, False, True))
        self.emit.printout(expr1)
        
        frame.enterLoop()
        labelContinue = frame.getContinueLabel()
        labelBreak = frame.getBreakLabel()
        
        expr2, _ = self.visit(ast.expr2, Access(frame, nenv, False, True))
        self.emit.printout(expr2)
        self.emit.printout(self.emit.emitIFFALSE(labelBreak, frame))
        
        self.visit(ast.loop, o)
        
        self.emit.printout(self.emit.emitLABEL(labelContinue,frame))
        
        if type(ast.expr3) is BinaryOp and ast.expr3.op == '=':
            self.visit(ast.expr3, Access(frame, nenv, False, True))
        else:
            expr3, _ = self.visit(ast.expr3, Access(frame, nenv, False, True))
            self.emit.printout(expr3)
            
        expr2, _ = self.visit(ast.expr2, Access(frame, nenv, False, True))
        self.emit.printout(expr2)
        self.emit.printout(self.emit.emitIFFALSE(labelBreak, frame))
        
        self.visit(ast.loop, o)
                  
        self.emit.printout(self.emit.emitGOTO(str(labelContinue), frame))
        self.emit.printout(self.emit.emitLABEL(labelBreak,frame))
        
        
    def visitBreak(self, ast, o):
        #o:any

        ctxt = o
        frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(), frame))

    def visitContinue(self, ast, o):
        #o:any
        
        ctxt = o
        frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame))
    
    def visitReturn(self, ast, o):
        #o:any
        #ast.expr: Expr

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        
        if ast.expr is not None:
            str1, typ1 = self.visit(ast.expr, Access(frame, nenv, False, True))
            if type(typ1) is IntType and type(frame.returnType) is FloatType:
                str1 += self.emit.emitI2F(frame)
            self.emit.printout(str1)
        #self.emit.printout(self.emit.emitGOTO(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(frame.returnType, frame))
        
    def visitArrayCell(self, ast, o):
        #o:any
        #ast.arr:Expr
        #ast.idx:Expr
        
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        lst = []
        arr, typeArr = self.visit(ast.arr, Access(frame, nenv, False, True))
        idx, typeIdx = self.visit(ast.idx, Access(frame, nenv, False, True))
        typ = typeArr.eleType
        lst.append(arr)
        lst.append(self.emit.emitPUSHICONST(typeArr.dimen - 1, frame))
        lst.append(idx)
        lst.append(self.emit.emitADDOP('-', IntType(), frame))
        if not o.isLeft:
            lst.append(self.emit.emitALOAD(typ, frame))
        return ''.join(lst), typ
        
    def visitBinaryOp(self, ast, o):
        #ast:BinaryOp
        #ast.op:str
        #ast.left:Expr
        #ast.right:Expr
        
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        
        leftOp, typeLHS = self.visit(ast.left, Access(frame, nenv, False, True))
        if type(ast.right) == CallExpr:
            self.visit(ast.right, Access(frame, nenv, False, True))
        else:                    
            rightOp, typeRHS = self.visit(ast.right, Access(frame, nenv, False, True))
        
        if ast.op == '=':
            if type(ast.left) is ArrayCell:
                leftOp, typeLHS = self.visit(ast.left, Access(frame, nenv, True, True))
                self.emit.printout(leftOp)
                if type(ast.right) == CallExpr:
                    self.visit(ast.right, Access(frame, nenv, False, True))
                else:
                    rightOp, typeRHS = self.visit(ast.right, Access(frame, nenv, False, True))
                    self.emit.printout(rightOp)
                if type(typeLHS) != type(typeRHS):
                    self.emit.printout(self.emit.emitI2F(frame))
                self.emit.printout(self.emit.emitASTORE(typeLHS, frame))          
            else:
                leftOp, typeLHS = self.visit(ast.left, Access(frame, nenv, True, True))
                if type(ast.right) == CallExpr:
                    self.visit(ast.right, Access(frame, nenv, False, True))
                else:
                    rightOp, typeRHS = self.visit(ast.right, Access(frame, nenv, False, True))
                    if type(typeRHS) is IntType and type(typeLHS) is FloatType:
                        rightOp += self.emit.emitI2F(frame)
                    self.emit.printout(rightOp + leftOp)
        elif type(typeLHS) == type(typeRHS):
            if type(typeLHS) is BoolType:
                if ast.op.lower() == '&&':
                    return leftOp + rightOp + self.emit.emitANDOP(frame), BoolType()   
                elif ast.op.lower() == '||':
                    return leftOp + rightOp + self.emit.emitOROP(frame), BoolType()
                elif ast.op in ['==','!=']:
                    return leftOp + rightOp + self.emit.emitREOP(ast.op, BoolType(), frame), BoolType()
            elif type(typeLHS) is IntType:
                if ast.op in ['+', '-']:
                    return leftOp + rightOp + self.emit.emitADDOP(ast.op, IntType(), frame), IntType()
                elif ast.op == '*':
                    return leftOp + rightOp + self.emit.emitMULOP(ast.op, IntType(), frame), IntType()
                elif ast.op == '/':
                    return leftOp + rightOp + self.emit.emitDIV(frame), IntType()
                elif ast.op == '%':
                    return leftOp + rightOp + self.emit.emitMOD(frame), IntType()
                elif ast.op in ['<', '<=', '>', '>=', '!=', '==']:
                    return leftOp + rightOp + self.emit.emitREOP(ast.op, IntType(), frame), BoolType()
            elif type(typeLHS) is FloatType:
                if ast.op in ['+', '-']:
                    return leftOp + rightOp + self.emit.emitADDOP(ast.op, FloatType(), frame), FloatType()
                elif ast.op == '*':
                    return leftOp + rightOp + self.emit.emitMULOP(ast.op, FloatType(), frame), FloatType()
                elif ast.op == '/':
                    return leftOp + rightOp + self.emit.emitMULOP(ast.op, FloatType(), frame), FloatType()
                elif ast.op in ['<', '<=', '>', '>=', '!=', '==']:
                    return self.emit.emitFREOP(ast.op, leftOp, rightOp, frame), BoolType()
        else:
            if ast.op in ['+', '-']:
                if type(typeLHS) is FloatType and type(typeRHS) is IntType:
                    return leftOp + rightOp + self.emit.emitI2F(frame) + self.emit.emitADDOP(ast.op, FloatType(), frame), FloatType()
                elif type(typeLHS) is IntType and type(typeRHS) is FloatType:
                    return leftOp + self.emit.emitI2F(frame) + rightOp + self.emit.emitADDOP(ast.op, FloatType(), frame), FloatType()
            elif ast.op == '*':
                if type(typeLHS) is FloatType and type(typeRHS) is IntType:
                    return leftOp + rightOp + self.emit.emitI2F(frame) + self.emit.emitMULOP(ast.op, FloatType(), frame), FloatType()
                elif type(typeLHS) is IntType and type(typeRHS) is FloatType:
                    return leftOp + self.emit.emitI2F(frame) + rightOp + self.emit.emitMULOP(ast.op, FloatType(), frame), FloatType()
            else:
                if type(typeLHS) is IntType: 
                    leftOp += self.emit.emitI2F(frame)
                if type(typeRHS) is IntType: 
                    rightOp += self.emit.emitI2F(frame)
                if ast.op == '/':
                    return leftOp + rightOp + self.emit.emitMULOP(ast.op, FloatType(), frame), FloatType()
                elif ast.op in ['<', '<=', '>', '>=', '!=', '==']:
                    return self.emit.emitFREOP(ast.op, leftOp, rightOp, frame), BoolType()
       
    def visitUnaryOp(self, ast, o):
        #o: Any
        #ast.op: string
        #ast.body: Expr
        
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        body, typ = self.visit(ast.body, Access(frame, nenv, False, True))
        if ast.op == '!' and type(typ) is BoolType:
            return body + self.emit.emitNOT(IntType(), frame), BoolType()
        elif ast.op == '-' and type(typ) is IntType:
            return body + self.emit.emitNEGOP(IntType(), frame), IntType()
        elif ast.op == '-' and type(typ) is FloatType:
            return body + self.emit.emitNEGOP(FloatType(), frame), FloatType()
        
    def visitCallExpr(self, ast, o):
        #ast: CallExpr
        #o: Any

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
        cname = sym.value.value
    
        ctype = sym.mtype

        in_ = ("", [])
        for x in ast.param:
            if type(x) is CallExpr:
                self.visit(x, Access(frame, nenv, False, True))
            else:
                str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
                in_ = (in_[0] + str1, in_[1] + [typ1])
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame))
    
    def visitId(self, ast, o):
        #o: Any
        #ast.name: string
        
        sym = self.lookup(ast.name, o.sym, lambda x: x.name)
        
        typ = sym.mtype

        if o.isLeft:
            if type(sym.value) is CName:
                return self.emit.emitPUTSTATIC(sym.value.value + "/" + sym.name, typ, o.frame), typ
            else:
                return self.emit.emitWRITEVAR(sym.name, typ, sym.value.value, o.frame), typ
        else:
            if type(sym.value) is CName:
                return self.emit.emitGETSTATIC(sym.value.value + "/" + sym.name, typ, o.frame), typ
            else:
                return self.emit.emitREADVAR(sym.name, typ, sym.value.value, o.frame), typ
                
    def visitIntLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

    def visitFloatLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()
        
    def visitBooleanLiteral(self, ast, o):
        #ast: BooleanLiteral
        #o: Any
        
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHCONST(str(ast.value).lower(), IntType(), frame), BoolType()
        
    def visitStringLiteral(self, ast, o):
        #ast: StringLiteral
        #o: Any
        
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHCONST('''"''' + ast.value + '''"''', StringType(), frame), StringType()
    
