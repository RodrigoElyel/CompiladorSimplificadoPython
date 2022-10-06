# Generated from C:/Users/rodri/OneDrive/�rea de Trabalho/Compiladores/Atividade 03\compiladorFinal.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .compiladorFinalParser import compiladorFinalParser
else:
    from compiladorFinalParser import compiladorFinalParser
from JasminGenerator import Generator, Id

# This class defines a complete listener for a parse tree produced by compiladorFinalParser.
class MyListener(ParseTreeListener):

    symbol_table = {}
    functions_args = {}
    stack_block = []

    def __init__(self, filename):
        self.jasmin = Generator(filename, self.symbol_table)
        self.label_id = 0

    def __is_numeric(self, type):
        return (type == 'float') or (type == 'int') or (type == 'integer')

    def __is_inside_function(self):
        return 'function' in self.stack_block

    # Enter a parse tree produced by compiladorFinalParser#prog.
    def enterProg(self, ctx: compiladorFinalParser.ProgContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#prog.
    def exitProg(self, ctx: compiladorFinalParser.ProgContext):
        self.jasmin.close_file()
        pass

    # Enter a parse tree produced by compiladorFinalParser#blockMain.
    def enterBlockMain(self, ctx: compiladorFinalParser.BlockMainContext):
        self.jasmin.enter_main()
        pass

    # Exit a parse tree produced by compiladorFinalParser#blockMain.
    def exitBlockMain(self, ctx: compiladorFinalParser.BlockMainContext):
        self.jasmin.exit_main()
        pass

    # Enter a parse tree produced by compiladorFinalParser#block.
    def enterBlock(self, ctx: compiladorFinalParser.BlockContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#block.
    def exitBlock(self, ctx: compiladorFinalParser.BlockContext):
        pass

    # Enter a parse tree produced by compiladorFinalParser#blockVoid.
    def enterBlockVoid(self, ctx: compiladorFinalParser.BlockVoidContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#blockVoid.
    def exitBlockVoid(self, ctx: compiladorFinalParser.BlockVoidContext):
        pass

    # Enter a parse tree produced by compiladorFinalParser#decVars.
    def enterDecVars(self, ctx: compiladorFinalParser.DecVarsContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#decVars.
    def exitDecVars(self, ctx: compiladorFinalParser.DecVarsContext):
        for token in ctx.ID():
            if token.getText() in self.symbol_table:
                raise AlreadyDeclaredError(ctx.start.line, token.getText())
            self.symbol_table[token.getText()] = Id(type=ctx.TYPE().getText())
            # if self.symbol_table[token.getText()].type == 'int':
            #     self.symbol_table[token.getText()].type = 'integer'
            self.jasmin.create_global(token.getText(), ctx.TYPE().getText())
        pass

    # Enter a parse tree produced by compiladorFinalParser#func_type.
    def enterFunc_type(self, ctx:compiladorFinalParser.Func_typeContext):
        self.stack_block.append('function')
        function_id = ctx.ID(0).getText()
        if function_id in self.symbol_table:
            raise AlreadyDeclaredError(ctx.start.line, function_id)

        self.symbol_table[function_id] = Id(type=ctx.TYPE(0).getText())
        # if self.symbol_table[function_id].type == 'int':
        #     self.symbol_table[function_id].type = 'integer'

        args = []
        args_names = []
        for arg_id, arg_type in list(zip(ctx.ID()[1:], ctx.TYPE()[1:])):
            if arg_id.getText() in self.symbol_table:
                raise AlreadyDeclaredError(ctx.start.line, arg_id.getText())
            self.symbol_table[arg_id.getText()] = Id(type=arg_type.getText(), local=True)
            args.append(arg_type.getText())
            args_names.append(arg_id.getText())

        self.functions_args[function_id] = args
        self.jasmin.enter_function(function_id, args_names)
        pass

    # Exit a parse tree produced by compiladorFinalParser#func_type.
    def exitFunc_type(self, ctx:compiladorFinalParser.Func_typeContext):
        # saindo da função antes de apagar referencias que podem ser importantes
        # TODO : verificar se existe retorno!!
        self.jasmin.exit_function()

        self.stack_block.pop()
        # for arg_id in ctx.ID()[1:]:
        #     del self.symbol_table[arg_id.getText()]
        pass


    # Enter a parse tree produced by compiladorFinalParser#func_void.
    def enterFunc_void(self, ctx:compiladorFinalParser.Func_voidContext):
        self.stack_block.append('function')
        function_id = ctx.ID(0).getText()
        if function_id in self.symbol_table:
            raise AlreadyDeclaredError(ctx.start.line, function_id)

        self.symbol_table[function_id] = Id(type="NoneType")
        # if self.symbol_table[function_id].type == 'int':
        #     self.symbol_table[function_id].type = 'integer'

        args = []
        args_names = []
        for arg_id, arg_type in list(zip(ctx.ID()[1:], ctx.TYPE()[0:])):
            if arg_id.getText() in self.symbol_table:
                raise AlreadyDeclaredError(ctx.start.line, arg_id.getText())
            self.symbol_table[arg_id.getText()] = Id(type=arg_type.getText(), local=True)
            args.append(arg_type.getText())
            args_names.append(arg_id.getText())

        self.functions_args[function_id] = args
        self.jasmin.enter_function(function_id, args_names)
        pass

    # Exit a parse tree produced by compiladorFinalParser#func_void.
    def exitFunc_void(self, ctx:compiladorFinalParser.Func_voidContext):
        self.jasmin.do_return(None, 'NoneType')
        self.jasmin.exit_function()

        self.stack_block.pop()

        # for arg_id in ctx.ID()[1:]:
        #     del self.symbol_table[arg_id.getText()]
        pass

    # Enter a parse tree produced by compiladorFinalParser#decFunctions.
    def enterDecFunctions(self, ctx: compiladorFinalParser.DecFunctionsContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#decFunctions.
    def exitDecFunctions(self, ctx: compiladorFinalParser.DecFunctionsContext):
        pass

    # Enter a parse tree produced by compiladorFinalParser#func_return.
    def enterFunc_return(self, ctx: compiladorFinalParser.Func_returnContext):
        if not self.__is_inside_function():
            raise ReturnException(ctx.start.line)
        pass

    # Exit a parse tree produced by compiladorFinalParser#func_return.
    def exitFunc_return(self, ctx: compiladorFinalParser.Func_returnContext):
        # TODO : conferir se o tipo do retorno bate com o da função
        self.jasmin.do_return(ctx.expr().val, ctx.expr().type)
        pass

    # Enter a parse tree produced by compiladorFinalParser#func_for.
    def enterFunc_for(self, ctx: compiladorFinalParser.Func_forContext):
        ctx_id = ctx.ID().getText()
        if ctx_id not in self.symbol_table:
            raise UndeclaredVariable(ctx.start.line, ctx_id)

        if not self.__is_numeric(self.symbol_table[ctx_id].type):
            raise UnexpectedTypeError(ctx.start.line, 'int', self.symbol_table[ctx_id].type)

        # ctx.expr()[len(ctx.expr()) - 1].inh = self.jasmin.enter_for(len(ctx.expr()) == 1)
        if len(ctx.expr()) == 1:
            ctx.expr()[0].inh_type = 'right_range'
            ctx.expr()[0].inh = self.jasmin.enter_for(len(self.stack_block), True, ctx_id)
        else:
            ctx.expr()[0].inh_type = 'left_range'
            ctx.expr()[1].inh_type = 'right_range'
            ctx.expr()[0].inh = ctx_id
            ctx.expr()[1].inh = self.jasmin.enter_for(len(self.stack_block), False, ctx_id)
        ctx.stack_idx = len(self.stack_block)

        self.stack_block.append('loop')
        pass

    # Exit a parse tree produced by compiladorFinalParser#func_for.
    def exitFunc_for(self, ctx: compiladorFinalParser.Func_forContext):
        self.stack_block.pop()

        ctx_id = ctx.ID().getText()
        if len(ctx.expr()) == 1:
            self.jasmin.exit_for(ctx_id, ctx.expr()[0].val, ctx.stack_idx)
        else:
            self.jasmin.exit_for(ctx_id, ctx.expr()[1].val, ctx.stack_idx)
        pass

    # Enter a parse tree produced by compiladorFinalParser#func_do_while.
    def enterFunc_do_while(self, ctx: compiladorFinalParser.Func_do_whileContext):
        ctx.expr().inh_type = 'while'
        ctx.expr().inh = self.jasmin.enter_while(len(self.stack_block))
        self.stack_block.append('loop')
        pass

    # Exit a parse tree produced by compiladorFinalParser#func_do_while.
    def exitFunc_do_while(self, ctx: compiladorFinalParser.Func_do_whileContext):
        if ctx.expr().type != 'boolean':
            raise UnexpectedTypeError(ctx.start.line, 'boolean', ctx.expr().type)
        self.stack_block.pop()
        self.jasmin.exit_while(len(self.stack_block))
        # verificar se é isso mesmo
        pass

    # Enter a parse tree produced by compiladorFinalParser#func_break.
    def enterFunc_break(self, ctx: compiladorFinalParser.Func_breakContext):
        if 'loop' not in self.stack_block:
            raise BreakException(ctx.start.line)
        pass

    # Exit a parse tree produced by compiladorFinalParser#func_break.
    def exitFunc_break(self, ctx: compiladorFinalParser.Func_breakContext):
        self.jasmin.break_loop(len(self.stack_block) - 1)
        pass

    # Enter a parse tree produced by compiladorFinalParser#func_if.
    def enterFunc_if(self, ctx: compiladorFinalParser.Func_ifContext):
        ctx.expr().inh_type = 'if'
        pass

    # Exit a parse tree produced by compiladorFinalParser#func_if.
    def exitFunc_if(self, ctx: compiladorFinalParser.Func_ifContext):
        if ctx.expr().type != 'boolean':
            raise UnexpectedTypeError(ctx.start.line, 'boolean', ctx.expr().type)
        self.jasmin.make_label('if_' + str(ctx.expr().end_label))
        pass

    # Enter a parse tree produced by compiladorFinalParser#func_else.
    def enterFunc_else(self, ctx: compiladorFinalParser.Func_elseContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#func_else.
    def exitFunc_else(self, ctx: compiladorFinalParser.Func_elseContext):
        pass

    # Enter a parse tree produced by compiladorFinalParser#func_print.
    def enterFunc_print(self, ctx: compiladorFinalParser.Func_printContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#func_print.
    def exitFunc_print(self, ctx: compiladorFinalParser.Func_printContext):
        type_val = []
        for expr in ctx.expr():
            type_val.append((expr.type, expr.val))
        self.jasmin.print(type_val)
        pass

    # Enter a parse tree produced by compiladorFinalParser#function_call.
    def enterFunction_call(self, ctx: compiladorFinalParser.Function_callContext):
        ctx_id = ctx.ID().getText()
        if ctx_id not in self.symbol_table:
            raise UndeclaredVariable(ctx.start.line, ctx_id)
        pass

    # Exit a parse tree produced by compiladorFinalParser#function_call.
    def exitFunction_call(self, ctx: compiladorFinalParser.Function_callContext):
        function_id = ctx.ID().getText()

        if len(self.functions_args[function_id]) != len(ctx.expr()):
            raise MissingArgument(ctx.start.line, len(self.functions_args[function_id]), len(ctx.expr()))

        for expected, recieved in list(zip(self.functions_args[function_id], ctx.expr())):
            if expected != recieved.type:
                raise UnexpectedTypeError(ctx.start.line, expected, recieved.type)

        ctx.type = self.symbol_table[ctx.ID().getText()].type
        pass

    # Enter a parse tree produced by compiladorFinalParser#assigment_expr.
    def enterAssigment_expr(self, ctx: compiladorFinalParser.Assigment_exprContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#assigment_expr.
    def exitAssigment_expr(self, ctx: compiladorFinalParser.Assigment_exprContext):
        ctx_id = ctx.ID().getText()
        if ctx_id not in self.symbol_table:
            raise UndeclaredVariable(ctx.start.line, ctx_id)

        expected = self.symbol_table[ctx_id].type
        recieved = ctx.expr().type
        # if recieved == 'int':
        #     recieved = 'integer'
        if expected != recieved:
            raise UnexpectedTypeError(ctx.start.line, expected, recieved)

        self.jasmin.store_var(ctx_id, ctx.expr().val)
        pass

    # Enter a parse tree produced by compiladorFinalParser#assigment_input.
    def enterAssigment_input(self, ctx: compiladorFinalParser.Assigment_inputContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#assigment_input.
    def exitAssigment_input(self, ctx: compiladorFinalParser.Assigment_inputContext):
        ctx_id = ctx.ID().getText()
        if ctx_id not in self.symbol_table:
            raise UndeclaredVariable(ctx.start.line, ctx_id)

        self.jasmin.input(ctx_id)
        pass

    # Enter a parse tree produced by compiladorFinalParser#operation_or.
    def enterOperation_or(self, ctx: compiladorFinalParser.Operation_orContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#operation_or.
    def exitOperation_or(self, ctx: compiladorFinalParser.Operation_orContext):
        if ctx.expr().type != 'boolean':
            raise ExprTypeError(ctx.start.line, ctx.op.text, ctx.expr().type)
        elif ctx.term().type != 'boolean':
            raise ExprTypeError(ctx.start.line, ctx.op.text, ctx.term().type)
        else:
            ctx.type = 'boolean'

        ctx.val = self.jasmin.calc_or(ctx.expr().val, ctx.term().val)

        if ctx.inh_type == 'while':
            self.jasmin.write_inh(ctx.inh.format(ctx.val))
        pass

    # Enter a parse tree produced by compiladorFinalParser#go_term.
    def enterGo_term(self, ctx: compiladorFinalParser.Go_termContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#go_term.
    def exitGo_term(self, ctx: compiladorFinalParser.Go_termContext):
        ctx.type = ctx.term().type
        ctx.val = ctx.term().val

        if ctx.inh_type == 'left_range':
            self.jasmin.store_var(ctx.inh, ctx.val)
        elif ctx.inh_type == 'right_range':
            self.jasmin.write_inh(ctx.inh)
        elif ctx.inh_type == 'while':
            self.jasmin.write_inh(ctx.inh.format(ctx.val))
        elif ctx.inh_type == 'if':
            ctx.end_label = self.jasmin.enter_if(ctx.val)
        pass

    # Enter a parse tree produced by compiladorFinalParser#go_term2.
    def enterGo_term2(self, ctx: compiladorFinalParser.Go_term2Context):
        pass

    # Exit a parse tree produced by compiladorFinalParser#go_term2.
    def exitGo_term2(self, ctx: compiladorFinalParser.Go_term2Context):
        ctx.type = ctx.term2().type
        ctx.val = ctx.term2().val
        pass

    # Enter a parse tree produced by compiladorFinalParser#operation_and.
    def enterOperation_and(self, ctx: compiladorFinalParser.Operation_andContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#operation_and.
    def exitOperation_and(self, ctx: compiladorFinalParser.Operation_andContext):
        if ctx.term().type != 'boolean':
            raise ExprTypeError(ctx.start.line, ctx.op.text, ctx.term().type)
        elif ctx.term2().type != 'boolean':
            raise ExprTypeError(ctx.start.line, ctx.op.text, ctx.term2().type)
        else:
            ctx.type = 'boolean'

        ctx.val = self.jasmin.calc_and(ctx.term().val, ctx.term2().val)
        pass

    # Enter a parse tree produced by compiladorFinalParser#operation_comparation.
    def enterOperation_comparation(self, ctx: compiladorFinalParser.Operation_comparationContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#operation_comparation.
    def exitOperation_comparation(self, ctx: compiladorFinalParser.Operation_comparationContext):
        if ctx.term2().type != ctx.term3().type:
            raise ExprTypeError(ctx.start.line, ctx.op.text, ctx.term2().type, ctx.term3().type)
        ctx.type = 'boolean'
        ctx.val = self.jasmin.calc_eq(ctx.term2().type, ctx.term2().val, ctx.term3().val, self.label_id, ctx.op.text)
        self.label_id += 1
        pass

    # Enter a parse tree produced by compiladorFinalParser#go_term3.
    def enterGo_term3(self, ctx: compiladorFinalParser.Go_term3Context):
        pass

    # Exit a parse tree produced by compiladorFinalParser#go_term3.
    def exitGo_term3(self, ctx: compiladorFinalParser.Go_term3Context):
        ctx.type = ctx.term3().type
        ctx.val = ctx.term3().val
        pass

    # Enter a parse tree produced by compiladorFinalParser#operation_equal_dif.
    def enterOperation_equal_dif(self, ctx: compiladorFinalParser.Operation_equal_difContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#operation_equal_dif.
    def exitOperation_equal_dif(self, ctx: compiladorFinalParser.Operation_equal_difContext):
        if ctx.term3().type != ctx.term4().type:
            raise ExprTypeError(ctx.start.line, ctx.op.text, ctx.term3().type, ctx.term4().type)
        ctx.type = 'boolean'
        ctx.val = self.jasmin.calc_eq(ctx.term3().type, ctx.term3().val, ctx.term4().val, self.label_id, ctx.op.text)
        self.label_id += 1
        pass

    # Enter a parse tree produced by compiladorFinalParser#go_term4.
    def enterGo_term4(self, ctx: compiladorFinalParser.Go_term4Context):
        pass

    # Exit a parse tree produced by compiladorFinalParser#go_term4.
    def exitGo_term4(self, ctx: compiladorFinalParser.Go_term4Context):
        ctx.type = ctx.term4().type
        ctx.val = ctx.term4().val
        pass

    # Enter a parse tree produced by compiladorFinalParser#operation_plus_sub.
    def enterOperation_plus_sub(self, ctx: compiladorFinalParser.Operation_plus_subContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#operation_plus_sub.
    def exitOperation_plus_sub(self, ctx: compiladorFinalParser.Operation_plus_subContext):
        if not self.__is_numeric(ctx.term4().type):
            raise ExprTypeError(ctx.start.line, ctx.op.text, ctx.term4().type)
        elif not self.__is_numeric(ctx.term5().type):
            raise ExprTypeError(ctx.start.line, ctx.op.text, ctx.term5().type)
        elif ctx.term4().type == 'float' and ctx.term5().type == 'float':
            ctx.type = 'float'
            val1, val2 = ctx.term4().val, ctx.term5().val
        elif ctx.term4().type == 'float':
            ctx.type = 'float'
            val1, val2 = ctx.term4().val, self.jasmin.int_to_float(ctx.term5().val)
        elif ctx.term5().type == 'float':
            ctx.type = 'float'
            val1, val2 = self.jasmin.int_to_float(ctx.term4().val), ctx.term5().val
        else:
            ctx.type = 'int'
            val1, val2 = ctx.term4().val, ctx.term5().val

        if ctx.op.text == '+':
            ctx.val = self.jasmin.add(ctx.type, val1, val2)
        else:
            ctx.val = self.jasmin.sub(ctx.type, val1, val2)
        pass

    # Enter a parse tree produced by compiladorFinalParser#go_term5.
    def enterGo_term5(self, ctx: compiladorFinalParser.Go_term5Context):
        pass

    # Exit a parse tree produced by compiladorFinalParser#go_term5.
    def exitGo_term5(self, ctx: compiladorFinalParser.Go_term5Context):
        ctx.type = ctx.term5().type
        ctx.val = ctx.term5().val
        pass

    # Enter a parse tree produced by compiladorFinalParser#go_term6.
    def enterGo_term6(self, ctx: compiladorFinalParser.Go_term6Context):
        pass

    # Exit a parse tree produced by compiladorFinalParser#go_term6.
    def exitGo_term6(self, ctx: compiladorFinalParser.Go_term6Context):
        ctx.type = ctx.term6().type
        ctx.val = ctx.term6().val
        pass

    # Enter a parse tree produced by compiladorFinalParser#operation_multi_div.
    def enterOperation_multi_div(self, ctx: compiladorFinalParser.Operation_multi_divContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#operation_multi_div.
    def exitOperation_multi_div(self, ctx: compiladorFinalParser.Operation_multi_divContext):
        if not self.__is_numeric(ctx.term5().type):
            raise ExprTypeError(ctx.start.line, ctx.op.text, ctx.term5().type)
        if not self.__is_numeric(ctx.term6().type):
            raise ExprTypeError(ctx.start.line, ctx.op.text, ctx.term6().type)
        elif ctx.term5().type == 'float' and ctx.term6().type == 'float':
            ctx.type = 'float'
            val1, val2 = ctx.term5().val, ctx.term6().val
        elif ctx.term5().type == 'float':
            ctx.type = 'float'
            val1, val2 = ctx.term5().val, self.jasmin.int_to_float(ctx.term6().val)
        elif ctx.term6().type == 'float':
            ctx.type = 'float'
            val1, val2 = self.jasmin.int_to_float(ctx.term5().val), ctx.term6().val
        else:
            ctx.type = 'int'
            val1, val2 = ctx.term5().val, ctx.term6().val

        if ctx.op.text == '*':
            ctx.val = self.jasmin.mul(ctx.type, val1, val2)
        else:
            ctx.val = self.jasmin.div(ctx.type, val1, val2)
        pass

    # Enter a parse tree produced by compiladorFinalParser#operation_minus_not.
    def enterOperation_minus_not(self, ctx: compiladorFinalParser.Operation_minus_notContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#operation_minus_not.
    def exitOperation_minus_not(self, ctx: compiladorFinalParser.Operation_minus_notContext):
        if ctx.op.text == '-':  # minus
            if self.__is_numeric(ctx.term6().type):
                ctx.type = ctx.term6().type
            else:
                raise ExprTypeError(ctx.start.line, ctx.op.text, ctx.term6().type)
        elif ctx.op.text == 'not':  # not
            if ctx.term6().type == 'boolean':
                ctx.type = 'boolean'
            else:
                raise ExprTypeError(ctx.start.line, ctx.op.text, ctx.term6().type)

            ctx.val = self.jasmin.calc_not(ctx.term6().val)
        pass

    # Enter a parse tree produced by compiladorFinalParser#go_factor.
    def enterGo_factor(self, ctx: compiladorFinalParser.Go_factorContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#go_factor.
    def exitGo_factor(self, ctx: compiladorFinalParser.Go_factorContext):
        ctx.type = ctx.factor().type
        ctx.val = ctx.factor().val
        pass

    # Enter a parse tree produced by compiladorFinalParser#terminal_openClose_expr.
    def enterTerminal_openClose_expr(self, ctx: compiladorFinalParser.Terminal_openClose_exprContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#terminal_openClose_expr.
    def exitTerminal_openClose_expr(self, ctx: compiladorFinalParser.Terminal_openClose_exprContext):
        ctx.type = ctx.expr().type
        ctx.val = ctx.expr().val
        pass

    # Enter a parse tree produced by compiladorFinalParser#terminal_id.
    def enterTerminal_id(self, ctx: compiladorFinalParser.Terminal_idContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#terminal_id.
    def exitTerminal_id(self, ctx: compiladorFinalParser.Terminal_idContext):
        ctx_id = ctx.ID().getText()
        if ctx_id not in self.symbol_table:
            raise UndeclaredVariable(ctx.start.line, ctx_id)
        ctx.type = self.symbol_table[ctx_id].type
        ctx.val = self.jasmin.load_var(ctx_id)
        pass

    # Enter a parse tree produced by compiladorFinalParser#terminal_int.
    def enterTerminal_int(self, ctx: compiladorFinalParser.Terminal_intContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#terminal_int.
    def exitTerminal_int(self, ctx: compiladorFinalParser.Terminal_intContext):
        ctx.type = 'int'
        ctx.val = self.jasmin.create_temp(ctx.getText(), ctx.type)
        pass

    # Enter a parse tree produced by compiladorFinalParser#terminal_float.
    def enterTerminal_float(self, ctx: compiladorFinalParser.Terminal_floatContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#terminal_float.
    def exitTerminal_float(self, ctx: compiladorFinalParser.Terminal_floatContext):
        ctx.type = 'float'
        ctx.val = self.jasmin.create_temp(ctx.getText(), ctx.type)
        pass

    # Enter a parse tree produced by compiladorFinalParser#terminal_string.
    def enterTerminal_string(self, ctx: compiladorFinalParser.Terminal_stringContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#terminal_string.
    def exitTerminal_string(self, ctx: compiladorFinalParser.Terminal_stringContext):
        ctx.type = 'string'
        ctx.val = self.jasmin.create_temp(ctx.getText(), ctx.type)
        pass

    # Enter a parse tree produced by compiladorFinalParser#terminal_boolean.
    def enterTerminal_boolean(self, ctx: compiladorFinalParser.Terminal_booleanContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#terminal_boolean.
    def exitTerminal_boolean(self, ctx: compiladorFinalParser.Terminal_booleanContext):
        ctx.type = 'boolean'
        ctx.val = self.jasmin.create_temp(0 if ctx.getText() == 'False' else 1, ctx.type)
        pass

    # Enter a parse tree produced by compiladorFinalParser#terminal_function_call.
    def enterTerminal_function_call(self, ctx: compiladorFinalParser.Terminal_function_callContext):
        pass

    # Exit a parse tree produced by compiladorFinalParser#terminal_function_call.
    def exitTerminal_function_call(self, ctx: compiladorFinalParser.Terminal_function_callContext):
        ctx.type = ctx.function_call().type
        ctx.val = ctx.function_call().val
        pass



del compiladorFinalParser

class ExprTypeError(Exception):
    def __init__(self, line, operation, type1, type2=None):
        message = 'Linha {}: Operação {} não suportada para os tipos: {} e {}'.format(line, operation, type1, type2) if type2 else 'Linha {}: Operação {} não suportada para o tipo: {}'.format(line, operation, type1)
        super().__init__(message)


class UndeclaredVariable(Exception):
    def __init__(self, line, id):
        message = 'Linha {}: A variável {} não foi declarada'.format(line, id)
        super().__init__(message)


class UnexpectedTypeError(Exception):
    def __init__(self, line, expected_type, recieved_type):
        message = 'Linha {}: Era esperado o tipo {}, foi recebido {}'.format(line, expected_type, recieved_type)
        super().__init__(message)


class BreakException(Exception):
    def __init__(self, line):
        message = 'Linha {}: Break fora do escopo de um laço de repetição'.format(line)
        super().__init__(message)


class ReturnException(Exception):
    def __init__(self, line):
        message = 'Linha {}: Return fora do escopo de uma função'.format(line)
        super().__init__(message)


class MissingArgument(Exception):
    def __init__(self, line, expected_args, recieved_args):
        message = 'Linha {}: Eram esperados {} argumentos, {} foram recebidos'.format(line, expected_args,
                                                                                      recieved_args)
        super().__init__(message)


class UndeclaredFunction(Exception):
    def __init__(self, line, id):
        message = 'Linha {}: A função {} não foi declarada'.format(line, id)
        super().__init__(message)


class AlreadyDeclaredError(Exception):
    def __init__(self, line, id):
        message = 'Linha {}: Id já declarado: {}'.format(line, id)
        super().__init__(message)
