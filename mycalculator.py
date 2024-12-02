from tkinter import *

# Create the main application window
root = Tk()
root.title("Calculator")

# Entry widget to display the input and output
input_entry = Entry(root, width=50)
input_entry.grid(columnspan=4)

def append_to_input(value):
    current_text = input_entry.get()
    input_entry.delete(0, END)
    input_entry.insert(0, current_text + value)

def evaluate_expression():
    try:
        expression = input_entry.get()
        result = eval(expression)
        input_entry.delete(0, END)
        input_entry.insert(0, str(result))
    except Exception as e:
        input_entry.delete(0, END)
        input_entry.insert(0, "Error")

# Create buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('0', 4, 0),
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
    ('=', 4, 2), ('.', 4, 1)
]

for (text, row, column) in buttons:
    if text == '=':
        button = Button(root, text=text, padx=40, pady=20, command=evaluate_expression)
    else:
        button = Button(root, text=text, padx=40, pady=20, command=lambda t=text: append_to_input(t))
    button.grid(row=row, column=column)

c_button=Button(root,text="Clear",command=lambda:input_entry.delete(0, END))
c_button.grid(row=5,columnspan=4)
# Run the application
root.mainloop()
