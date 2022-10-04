from antlr4 import *
from tkinter import *

from gen.compiladorFinalLexer import compiladorFinalLexer
from gen.compiladorFinalParser import compiladorFinalParser
from gen.compiladorFinalListener import compiladorFinalListener

if __name__ == '__main__':

    def Take_input():
        INPUT = inputtxt.get("1.0", "end-1c")
        data = InputStream(INPUT)

        # Lexer
        lexer = compiladorFinalLexer(data)
        tokens = CommonTokenStream(lexer)

        # Parser
        parser = exprAtv04Parser(tokens)
        tree = parser.line()

        # Listener
        listener = MyExprAtv04Listener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        Output.insert(END, '\n')
        Output.insert(END, 'Expressão --> {}\n'.format(listener.initial_expr))
        Output.insert(END,  'Resultado --> {}\n'.format(listener.final_result))
        Output.insert(END, '\n----------------------------------------------\n')


    root = Tk()
    root.geometry("800x800")
    root.title(" Atividade 04 ")

    l = Label(text="Digite seu código ")
    inputtxt = Text(root, height=10,
                    width=400,
                    bg="light yellow")

    Output = Text(root, height=400,
                  width=400,
                  bg="light cyan")

    Display = Button(root, height=2,
                     width=20,
                     text="Calcular",
                     command=lambda: Take_input())

    l.pack()
    inputtxt.pack()
    Display.pack()
    Output.pack()

    mainloop()



