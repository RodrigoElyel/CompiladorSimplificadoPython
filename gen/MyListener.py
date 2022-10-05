# Generated from C:/Users/rodri/OneDrive/�rea de Trabalho/Compiladores/Atividade 03\compiladorFinal.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .compiladorFinalParser import compiladorFinalParser
else:
    from compiladorFinalParser import compiladorFinalParser

# This class defines a complete listener for a parse tree produced by compiladorFinalParser.
class MyListener(ParseTreeListener):

    final_result = None
    initial_expr = ''


    # Enter a parse tree produced by compiladorFinalParser#prog.
    def enterProg(self, ctx:compiladorFinalParser.ProgContext):
        print(ctx.getText())
        self.initial_expr = ctx.getText()

    # Exit a parse tree produced by compiladorFinalParser#prog.
    def exitProg(self, ctx:compiladorFinalParser.ProgContext):
        pass


    # Enter a parse tree produced by compiladorFinalParser#blockMain.
    def enterBlockMain(self, ctx:compiladorFinalParser.BlockMainContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#blockMain.
    def exitBlockMain(self, ctx:compiladorFinalParser.BlockMainContext):
        pass


    # Enter a parse tree produced by compiladorFinalParser#block.
    def enterBlock(self, ctx:compiladorFinalParser.BlockContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#block.
    def exitBlock(self, ctx:compiladorFinalParser.BlockContext):
        pass


    # Enter a parse tree produced by compiladorFinalParser#blockVoid.
    def enterBlockVoid(self, ctx:compiladorFinalParser.BlockVoidContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#blockVoid.
    def exitBlockVoid(self, ctx:compiladorFinalParser.BlockVoidContext):
        pass


    # Enter a parse tree produced by compiladorFinalParser#decVars.
    def enterDecVars(self, ctx:compiladorFinalParser.DecVarsContext):
        print(ctx.TYPE(), ' TYPE')
        pass

    # Exit a parse tree produced by compiladorFinalParser#decVars.
    def exitDecVars(self, ctx:compiladorFinalParser.DecVarsContext):
        # print(ctx., ' getTokens')
        pass


    # Enter a parse tree produced by compiladorFinalParser#decFunctions.
    def enterDecFunctions(self, ctx:compiladorFinalParser.DecFunctionsContext):
        print(ctx.getTokens() + ' tokens')

        # if (ctx.op.text) == '*':
        #     ctx.val = ctx.term().val * ctx.factor().val
        # else:
        #     ctx.val = ctx.term().val / ctx.factor().val

    # Exit a parse tree produced by compiladorFinalParser#decFunctions.
    def exitDecFunctions(self, ctx:compiladorFinalParser.DecFunctionsContext):
        pass


    # Enter a parse tree produced by compiladorFinalParser#func_return.
    def enterFunc_return(self, ctx:compiladorFinalParser.Func_returnContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#func_return.
    def exitFunc_return(self, ctx:compiladorFinalParser.Func_returnContext):
        pass


    # Enter a parse tree produced by compiladorFinalParser#func_for.
    def enterFunc_for(self, ctx:compiladorFinalParser.Func_forContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#func_for.
    def exitFunc_for(self, ctx:compiladorFinalParser.Func_forContext):
        pass


    # Enter a parse tree produced by compiladorFinalParser#func_do_while.
    def enterFunc_do_while(self, ctx:compiladorFinalParser.Func_do_whileContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#func_do_while.
    def exitFunc_do_while(self, ctx:compiladorFinalParser.Func_do_whileContext):
        pass


    # Enter a parse tree produced by compiladorFinalParser#func_break.
    def enterFunc_break(self, ctx:compiladorFinalParser.Func_breakContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#func_break.
    def exitFunc_break(self, ctx:compiladorFinalParser.Func_breakContext):
        pass


    # Enter a parse tree produced by compiladorFinalParser#func_if.
    def enterFunc_if(self, ctx:compiladorFinalParser.Func_ifContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#func_if.
    def exitFunc_if(self, ctx:compiladorFinalParser.Func_ifContext):
        pass


    # Enter a parse tree produced by compiladorFinalParser#func_else.
    def enterFunc_else(self, ctx:compiladorFinalParser.Func_elseContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#func_else.
    def exitFunc_else(self, ctx:compiladorFinalParser.Func_elseContext):
        pass


    # Enter a parse tree produced by compiladorFinalParser#func_print.
    def enterFunc_print(self, ctx:compiladorFinalParser.Func_printContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#func_print.
    def exitFunc_print(self, ctx:compiladorFinalParser.Func_printContext):
        pass


    # Enter a parse tree produced by compiladorFinalParser#function_call.
    def enterFunction_call(self, ctx:compiladorFinalParser.Function_callContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#function_call.
    def exitFunction_call(self, ctx:compiladorFinalParser.Function_callContext):
        pass


    # Enter a parse tree produced by compiladorFinalParser#assigment.
    def enterAssigment(self, ctx:compiladorFinalParser.AssigmentContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#assigment.
    def exitAssigment(self, ctx:compiladorFinalParser.AssigmentContext):
        pass


    # Enter a parse tree produced by compiladorFinalParser#expr.
    def enterExpr(self, ctx:compiladorFinalParser.ExprContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#expr.
    def exitExpr(self, ctx:compiladorFinalParser.ExprContext):
        pass


    # Enter a parse tree produced by compiladorFinalParser#term.
    def enterTerm(self, ctx:compiladorFinalParser.TermContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#term.
    def exitTerm(self, ctx:compiladorFinalParser.TermContext):
        pass


    # Enter a parse tree produced by compiladorFinalParser#term2.
    def enterTerm2(self, ctx:compiladorFinalParser.Term2Context):
        pass

    # Exit a parse tree produced by compiladorFinalParser#term2.
    def exitTerm2(self, ctx:compiladorFinalParser.Term2Context):
        pass


    # Enter a parse tree produced by compiladorFinalParser#term3.
    def enterTerm3(self, ctx:compiladorFinalParser.Term3Context):
        pass

    # Exit a parse tree produced by compiladorFinalParser#term3.
    def exitTerm3(self, ctx:compiladorFinalParser.Term3Context):
        pass


    # Enter a parse tree produced by compiladorFinalParser#term4.
    def enterTerm4(self, ctx:compiladorFinalParser.Term4Context):
        pass

    # Exit a parse tree produced by compiladorFinalParser#term4.
    def exitTerm4(self, ctx:compiladorFinalParser.Term4Context):
        pass


    # Enter a parse tree produced by compiladorFinalParser#term5.
    def enterTerm5(self, ctx:compiladorFinalParser.Term5Context):
        pass

    # Exit a parse tree produced by compiladorFinalParser#term5.
    def exitTerm5(self, ctx:compiladorFinalParser.Term5Context):
        pass
        # if (ctx.op.text) == '*':
        #     ctx.val = ctx.term().val * ctx.factor().val
        # else:
        #     ctx.val = ctx.term().val / ctx.factor().val


    # Enter a parse tree produced by compiladorFinalParser#term6.
    def enterTerm6(self, ctx:compiladorFinalParser.Term6Context):
        pass

    # Exit a parse tree produced by compiladorFinalParser#term6.
    def exitTerm6(self, ctx:compiladorFinalParser.Term6Context):
        pass


    # Enter a parse tree produced by compiladorFinalParser#factor.
    def enterFactor(self, ctx:compiladorFinalParser.FactorContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#factor.
    def exitFactor(self, ctx:compiladorFinalParser.FactorContext):
        pass



del compiladorFinalParser
