import tkinter as tk
from math import sin, cos, tan, log, sqrt, pi, e, radians

class ScientificCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")
        master.configure(bg="#22252A")
        self.expression = ""
        self.text_input = tk.StringVar()
        self.last_answer = "0"  # default Ans = 0

       ############## Entry ############
        self.entry = tk.Entry(
            master, font=('Segoe UI', 24), textvariable=self.text_input,
            bd=0, bg="#292D36", fg="#FDF6E3", insertbackground="#FDF6E3",
            width=22, borderwidth=0, justify='right'
        )
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=(15, 10), sticky="nsew")

        ############### Buttons layout ###############
        btn_defs = [
            [('C', "#B20000", "#FFFFFF"), ('DEL', "#B20000", "#FFFFFF"), ('(', "#303136", "#FDF6E3"), (')', "#303136", "#FDF6E3"), ('√', "#6C29B2", "#FFFFFF")],
            [('7', "#303136", "#FDF6E3"), ('8', "#303136", "#FDF6E3"), ('9', "#303136", "#FDF6E3"), ('/', "#005DB2", "#FFFFFF"), ('log', "#6C29B2", "#FFFFFF")],
            [('4', "#303136", "#FDF6E3"), ('5', "#303136", "#FDF6E3"), ('6', "#303136", "#FDF6E3"), ('*', "#005DB2", "#FFFFFF"), ('sin', "#6C29B2", "#FFFFFF")],
            [('1', "#303136", "#FDF6E3"), ('2', "#303136", "#FDF6E3"), ('3', "#303136", "#FDF6E3"), ('-', "#005DB2", "#FFFFFF"), ('cos', "#6C29B2", "#FFFFFF")],
            [('0', "#303136", "#FDF6E3"), ('.', "#303136", "#FDF6E3"), ('=', "#00B289", "#FFFFFF"), ('+', "#005DB2", "#FFFFFF"), ('tan', "#6C29B2", "#FFFFFF")],
            [('π', "#6C29B2", "#FFFFFF"), ('e', "#6C29B2", "#FFFFFF"), ('^', "#005DB2", "#FFFFFF"), ('%', "#005DB2", "#FFFFFF"), ('Ans', "#00897b", "#FFFFFF")]
        ]

        ############### Create buttons ###############
        for i, row in enumerate(btn_defs):
            for j, (text, bg, fg) in enumerate(row):
                btn = tk.Button(
                    master, text=text, font=('Segoe UI', 18, 'bold'),
                    bg=bg, fg=fg, activebackground="#393E46", activeforeground="#FDF6E3",
                    bd=0, padx=0, pady=0, cursor="hand2",
                    command=lambda t=text: self.on_button_click(t)
                )
                btn.grid(row=i+1, column=j, sticky="nsew", padx=6, pady=6, ipadx=10, ipady=18)

        ############## Responsive resizing ##############
        for i in range(7):
            master.grid_rowconfigure(i, weight=1)
        for j in range(5):
            master.grid_columnconfigure(j, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.text_input.set("")
        elif char == 'DEL':
            self.expression = self.expression[:-1]
            self.text_input.set(self.expression)
        elif char == '=':
            try:
                expr = self.expression.replace('π', str(pi)).replace('√', 'sqrt').replace('^', '**')
                # handle percentage like calculator: "50%" -> "50/100"
                expr = expr.replace('%', '/100')

                result = str(eval(expr, {"__builtins__": None}, {
                    'sin': lambda x: sin(radians(x)),   # DEGREE MODE
                    'cos': lambda x: cos(radians(x)),
                    'tan': lambda x: tan(radians(x)),
                    'log': lambda x: log(x, 10),        # base-10 log
                    'sqrt': sqrt, 'pi': pi, 'e': e
                }))
                self.text_input.set(result)
                self.expression = result
                self.last_answer = result
            except Exception:
                self.text_input.set("Error")
                self.expression = ""
        elif char == 'π':
            self.expression += str(pi)
            self.text_input.set(self.expression)
        elif char == 'e':
            self.expression += str(e)
            self.text_input.set(self.expression)
        elif char == '√':
            self.expression += '√('
            self.text_input.set(self.expression)
        elif char in ['sin', 'cos', 'tan', 'log']:
            self.expression += char + '('
            self.text_input.set(self.expression)
        elif char == 'Ans':
            self.expression += str(self.last_answer)
            self.text_input.set(self.expression)
        else:
            self.expression += str(char)
            self.text_input.set(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(420, 600)
    calc = ScientificCalculator(root)
    root.mainloop()



