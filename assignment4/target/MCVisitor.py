# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#manyDecls.
    def visitManyDecls(self, ctx:MCParser.ManyDeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#decl.
    def visitDecl(self, ctx:MCParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#varDecl.
    def visitVarDecl(self, ctx:MCParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#var.
    def visitVar(self, ctx:MCParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcDecl.
    def visitFuncDecl(self, ctx:MCParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#returnType.
    def visitReturnType(self, ctx:MCParser.ReturnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#paraList.
    def visitParaList(self, ctx:MCParser.ParaListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#paraDecl.
    def visitParaDecl(self, ctx:MCParser.ParaDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#blockStmt.
    def visitBlockStmt(self, ctx:MCParser.BlockStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#blockMem.
    def visitBlockMem(self, ctx:MCParser.BlockMemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#stmt.
    def visitStmt(self, ctx:MCParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#ifStmt.
    def visitIfStmt(self, ctx:MCParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#dowhileStmt.
    def visitDowhileStmt(self, ctx:MCParser.DowhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#forStmt.
    def visitForStmt(self, ctx:MCParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#breakStmt.
    def visitBreakStmt(self, ctx:MCParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#contStmt.
    def visitContStmt(self, ctx:MCParser.ContStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#returnStmt.
    def visitReturnStmt(self, ctx:MCParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expStmt.
    def visitExpStmt(self, ctx:MCParser.ExpStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp.
    def visitExp(self, ctx:MCParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp1.
    def visitExp1(self, ctx:MCParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp2.
    def visitExp2(self, ctx:MCParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp3.
    def visitExp3(self, ctx:MCParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp4.
    def visitExp4(self, ctx:MCParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp5.
    def visitExp5(self, ctx:MCParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp6.
    def visitExp6(self, ctx:MCParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp7.
    def visitExp7(self, ctx:MCParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp8.
    def visitExp8(self, ctx:MCParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp9.
    def visitExp9(self, ctx:MCParser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#invokeExp.
    def visitInvokeExp(self, ctx:MCParser.InvokeExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#inArrPtrType.
    def visitInArrPtrType(self, ctx:MCParser.InArrPtrTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#outArrPtrType.
    def visitOutArrPtrType(self, ctx:MCParser.OutArrPtrTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#primType.
    def visitPrimType(self, ctx:MCParser.PrimTypeContext):
        return self.visitChildren(ctx)



del MCParser