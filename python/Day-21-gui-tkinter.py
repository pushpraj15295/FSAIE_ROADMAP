import ast
import operator
from tkinter import *


root = Tk()
root.title("Calculater")
root.geometry("360x540")
root.resizable(True, True)
root.configure(bg="#303134")

# On this Mac, Label and Canvas text does not show on a dark window.
# Button text does, so the two screens are buttons that only display text.
expression = StringVar(value="0")
result = StringVar(value="0")

screen = Button(
    root,
    textvariable=expression,
    font=("Helvetica", 32),
    bg="#202124",
    fg="white",
    activebackground="#202124",
    activeforeground="white",
    highlightbackground="#202124",
    relief="flat",
    anchor="e",
    borderwidth=0,
    command=lambda: None,
)
screen.grid(row=0, column=0, columnspan=5, sticky="ew", padx=12, pady=(16, 4), ipady=8)

result_label = Button(
    root,
    textvariable=result,
    font=("Helvetica", 20),
    bg="#202124",
    fg="#8ab4f8",
    activebackground="#202124",
    activeforeground="#8ab4f8",
    highlightbackground="#202124",
    relief="flat",
    anchor="e",
    borderwidth=0,
    command=lambda: None,
)

buttons = [
    ["7", "8", "9", "/", "C"],
    ["4", "5", "6", "*", "C"],
    ["1", "2", "3", "-", "="],
    ["0", ".", "+", "="],
]

ops = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}


def eval_node(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        value = eval_node(node.operand)
        return value if isinstance(node.op, ast.UAdd) else -value
    if isinstance(node, ast.BinOp) and type(node.op) in ops:
        return ops[type(node.op)](eval_node(node.left), eval_node(node.right))
    raise ValueError("unsupported expression")


def calculate(value):
    tree = ast.parse(value, mode="eval")
    return eval_node(tree.body)


def format_result(value):
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def on_button_click(value):
    current = expression.get()

    if value == "C":
        expression.set("0")
        result.set("0")
        return

    if value == "=":
        try:
            answer = format_result(calculate(current))
            expression.set(answer)
            result.set(answer)
        except Exception:
            result.set("Error")
        return

    if current == "0" and value not in ".+-*/":
        expression.set(value)
    else:
        expression.set(current + value)


for row, row_buttons in enumerate(buttons):
    for col, label in enumerate(row_buttons):
        button = Button(
            root,
            text=label,
            font=("Helvetica", 18),
            bg="#3c4043",
            fg="white",
            activebackground="#5f6368",
            activeforeground="white",
            highlightbackground="#3c4043",
            relief="flat",
            borderwidth=0,
            command=lambda v=label: on_button_click(v),
        )
        button.grid(row=row + 2, column=col, sticky="nsew", padx=6, pady=6, ipady=6)

for col in range(5):
    root.columnconfigure(col, weight=1)
for row in range(2, 6):
    root.rowconfigure(row, weight=1)

root.mainloop()
