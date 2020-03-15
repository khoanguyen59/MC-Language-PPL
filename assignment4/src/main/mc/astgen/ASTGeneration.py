from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *
import functools

class ASTGeneration(MCVisitor):
    def visitProgram(self,ctx:MCParser.ProgramContext):
        #program : manyDecls EOF; 
        return Program(self.visit(ctx.manyDecls()))
        
    def visitManyDecls(self,ctx:MCParser.ManyDeclsContext):
        #manyDecls: decl manyDecls | decl ; 
        if ctx.manyDecls(): 
            return self.visit(ctx.decl()) + self.visit(ctx.manyDecls())
        else: 
            return self.visit(ctx.decl())
            
    def visitDecl(self, ctx:MCParser.DeclContext):
        #decl: varDecl | funcDecl ;
        if type(self.visit(ctx.getChild(0))) == type([]):
            return self.visit(ctx.getChild(0))
        else:    
            return [self.visit(ctx.getChild(0))]
            
    def visitVarDecl(self, ctx:MCParser.VarDeclContext):
        #varDecl: primType var (COMMA var)* SEMI ;
        listVarDecl = []
        for x in ctx.var():
            if x.getChildCount() == 1:
                listVarDecl += [VarDecl(self.visit(x),self.visit(ctx.primType()))]         
            else:
                listVarDecl += [VarDecl(self.visit(x),ArrayType(int(x.INTLIT().getText()),self.visit(ctx.primType())))]
        return listVarDecl 
        #return [VarDecl(self.visit(x),self.visit(ctx.primType())) for x in ctx.var()] 
        #return list(map(lambda x: VarDecl(self.visit(x),self.visit(ctx.primType())), ctx.var()))
        
    def visitVar(self, ctx:MCParser.VarContext):
        #var: ID | ID LS INTLIT RS ;
        return ctx.ID().getText() 
        
    def visitFuncDecl(self, ctx:MCParser.FuncDeclContext):
        #funcDecl: returnType ID LB paraList? RB blockStmt;
        if ctx.paraList():
            return FuncDecl(Id(ctx.ID().getText()),self.visit(ctx.paraList()),self.visit(ctx.returnType()),self.visit(ctx.blockStmt()))
        else:
            return FuncDecl(Id(ctx.ID().getText()),[],self.visit(ctx.returnType()),self.visit(ctx.blockStmt()))
            
    def visitReturnType(self, ctx:MCParser.ReturnTypeContext):
        #returnType: primType | outArrPtrType | VOID ; 
        return self.visit(ctx.primType()) if ctx.primType() else self.visit(ctx.outArrPtrType()) if ctx.outArrPtrType() else VoidType()
        
    def visitParaList(self, ctx:MCParser.ParaListContext):
        #paraList: paraDecl COMMA paraList | paraDecl ;
        return self.visit(ctx.paraDecl()) + self.visit(ctx.paraList()) if ctx.paraList() else self.visit(ctx.paraDecl())
        
    def visitParaDecl(self, ctx:MCParser.ParaDeclContext):
        #paraDecl: primType ID | primType ID LS RS ;
        listParaDecl = []
        if ctx.getChildCount() == 2: 
            listParaDecl += [VarDecl(ctx.ID().getText(),self.visit(ctx.primType()))]
        else:
            listParaDecl += [VarDecl(ctx.ID().getText(),ArrayPointerType(self.visit(ctx.primType())))]
        return listParaDecl

    def visitBlockStmt(self, ctx:MCParser.BlockStmtContext):
        #blockStmt: LP (blockMem)* RP ;
        listBlockMember = []
        #if ctx.varDecl():
        #    for x in ctx.varDecl():
         #       listBlockMember += self.visit(x)
        #if ctx.stmt():    
         #   for y in ctx.stmt():
          #      listBlockMember += [self.visit(y)]
        for x in ctx.blockMem():
            if x.varDecl():
                listBlockMember += self.visit(x)
            else:
                listBlockMember += [self.visit(x)]
        return Block(listBlockMember)
        
    def visitStmt(self, ctx:MCParser.StmtContext):
        #stmt: ifStmt | dowhileStmt | forStmt | breakStmt | contStmt | returnStmt | expStmt | blockStmt ;
        return self.visit(ctx.getChild(0))
        
    def visitIfStmt(self, ctx:MCParser.IfStmtContext):
        #ifStmt: IF LB exp RB stmt (ELSE stmt)? ;
        if ctx.ELSE():
            return If(self.visit(ctx.exp()),self.visit(ctx.stmt(0)),self.visit(ctx.stmt(1)))
        else:
            return If(self.visit(ctx.exp()),self.visit(ctx.stmt(0)),)
        
    def visitDowhileStmt(self, ctx:MCParser.DowhileStmtContext):
        #dowhileStmt: DO (stmt)+ WHILE exp SEMI ;
        return Dowhile([self.visit(x) for x in ctx.stmt()],self.visit(ctx.exp()))
        
    def visitForStmt(self, ctx:MCParser.ForStmtContext):
        #forStmt: FOR LB exp SEMI exp SEMI exp RB stmt ;
        return For(self.visit(ctx.exp(0)),self.visit(ctx.exp(1)),self.visit(ctx.exp(2)),self.visit(ctx.stmt()))
       
    def visitBreakStmt(self, ctx:MCParser.BreakStmtContext):
        #breakStmt: BREAK SEMI ;
        return Break()
        
    def visitContStmt(self, ctx:MCParser.ContStmtContext):
        #contStmt: CONTINUE SEMI ;
        return Continue()  

    def visitReturnStmt(self, ctx:MCParser.ReturnStmtContext):
        #returnStmt: RETURN exp? SEMI ;
        if ctx.exp():
            return Return(self.visit(ctx.exp()))
        else:
            return Return()
     
    def visitExpStmt(self, ctx:MCParser.ExpStmtContext):
        #expStmt: exp SEMI ;
        return self.visit(ctx.exp())
        
    def visitPrimType(self, ctx:MCParser.PrimTypeContext):
        #primType:  INT | FLOAT | BOOLEAN | STRING ; 
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        else:
            return StringType()
            
    def visitOutArrPtrType(self, ctx:MCParser.OutArrPtrTypeContext):
        #outArrPtrType: primType LS RS ;
        return ArrayPointerType(self.visit(ctx.primType()))
        
    def visitExp(self, ctx:MCParser.ExpContext):
        #exp : exp1 ASSIGN exp | exp1 ;
        return BinaryOp(ctx.ASSIGN().getText(),self.visit(ctx.exp1()),self.visit(ctx.exp())) if ctx.ASSIGN() else self.visit(ctx.exp1())
        
    def visitExp1(self, ctx:MCParser.Exp1Context):
        #exp1: exp1 OR exp2 | exp2 ; 
        return BinaryOp(ctx.OR().getText(),self.visit(ctx.exp1()),self.visit(ctx.exp2())) if ctx.OR() else self.visit(ctx.exp2())
        
    def visitExp2(self, ctx:MCParser.Exp2Context):
        #exp2: exp2 AND exp3 | exp3 ;
        return BinaryOp(ctx.AND().getText(),self.visit(ctx.exp2()),self.visit(ctx.exp3())) if ctx.AND() else self.visit(ctx.exp3())

    def visitExp3(self, ctx:MCParser.Exp3Context):
        #exp3: exp4 EQ exp4 | exp4 NEQ exp4 | exp4 ;
        if ctx.EQ():
            return BinaryOp(ctx.EQ().getText(),self.visit(ctx.exp4(0)),self.visit(ctx.exp4(1)))
        elif ctx.NEQ():
            return BinaryOp(ctx.NEQ().getText(),self.visit(ctx.exp4(0)),self.visit(ctx.exp4(1)))
        else:
            return self.visit(ctx.exp4(0))
    
    def visitExp4(self, ctx:MCParser.Exp4Context):
        #exp4: exp5 LT exp5 | exp5 LEQ exp5 | exp5 GT exp5 | exp5 GEQ exp5 | exp5 ;
        if ctx.LT():
            return BinaryOp(ctx.LT().getText(),self.visit(ctx.exp5(0)),self.visit(ctx.exp5(1)))
        elif ctx.LEQ():
            return BinaryOp(ctx.LEQ().getText(),self.visit(ctx.exp5(0)),self.visit(ctx.exp5(1)))
        elif ctx.GT():
            return BinaryOp(ctx.GT().getText(),self.visit(ctx.exp5(0)),self.visit(ctx.exp5(1)))
        elif ctx.GEQ():
            return BinaryOp(ctx.GEQ().getText(),self.visit(ctx.exp5(0)),self.visit(ctx.exp5(1)))
        else:
            return self.visit(ctx.exp5(0)) 

    def visitExp5(self, ctx:MCParser.Exp5Context):
        #exp5: exp5 ADD exp6 | exp5 SUB exp6 | exp6 ;
        if ctx.ADD():
            return BinaryOp(ctx.ADD().getText(),self.visit(ctx.exp5()),self.visit(ctx.exp6()))
        elif ctx.SUB():
            return BinaryOp(ctx.SUB().getText(),self.visit(ctx.exp5()),self.visit(ctx.exp6()))
        else:
            return self.visit(ctx.exp6()) 
        
    def visitExp6(self, ctx:MCParser.Exp6Context):
        #exp6: exp6 DIV exp7 | exp6 MUL exp7 | exp6 MOD exp7 | exp7 ;
        if ctx.DIV():
            return BinaryOp(ctx.DIV().getText(),self.visit(ctx.exp6()),self.visit(ctx.exp7()))
        elif ctx.MUL():
            return BinaryOp(ctx.MUL().getText(),self.visit(ctx.exp6()),self.visit(ctx.exp7()))
        elif ctx.MOD():
            return BinaryOp(ctx.MOD().getText(),self.visit(ctx.exp6()),self.visit(ctx.exp7()))    
        else:
            return self.visit(ctx.exp7())  

    def visitExp7(self, ctx:MCParser.Exp7Context):
        #exp7: NOT exp7 | SUB exp7 | exp8 ;
        if ctx.NOT():
            return UnaryOp(ctx.NOT().getText(),self.visit(ctx.exp7()))
        elif ctx.SUB():
            return UnaryOp(ctx.SUB().getText(),self.visit(ctx.exp7()))  
        else:
            return self.visit(ctx.exp8())        

    def visitExp8(self, ctx:MCParser.Exp8Context):
        #exp8: exp9 LS exp RS | exp9 ;
        if ctx.exp():
            return ArrayCell(self.visit(ctx.exp9()),self.visit(ctx.exp()))
        else:
            return(self.visit(ctx.exp9()))
     
    def visitExp9(self, ctx:MCParser.Exp9Context):
        #exp9: LB exp RB | (INTLIT | FLOATLIT | BOOLEANLIT | STRINGLIT | ID | invokeExp) ;
        if ctx.getChildCount() == 3:
            return self.visit(ctx.exp())
        else:
            if ctx.INTLIT():
                return IntLiteral(int(ctx.INTLIT().getText()))
            elif ctx.FLOATLIT():
                return FloatLiteral(float(ctx.FLOATLIT().getText()))
            elif ctx.BOOLEANLIT():
                return BooleanLiteral(bool("1")) if ctx.BOOLEANLIT().getText() == "true" else BooleanLiteral(bool(""))
            elif ctx.STRINGLIT():
                return StringLiteral(ctx.STRINGLIT().getText())
            elif ctx.ID():
                return Id(ctx.ID().getText())
            else:
                return self.visit(ctx.invokeExp())
            
    def visitInvokeExp(self, ctx:MCParser.InvokeExpContext):
        #invokeExp: ID LB (exp (COMMA exp)*)? RB ; //callExpr
        if ctx.exp():
            return CallExpr(Id(ctx.ID().getText()),[self.visit(x) for x in ctx.exp()])
        else:
            return CallExpr(Id(ctx.ID().getText()),[])