from tkinter import *

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

root = Tk()
root.title("Calculator")
root.configure(bg="lightgrey")  # Set background color

equation = StringVar()

txt = Entry(root, textvariable=equation, font=('Arial', 18), bd=5, relief="ridge")
txt.grid(columnspan=4, ipadx=8, ipady=5)

# Button colors
num_color = "lightblue"
op_color = "orange"
clear_color = "red"
equal_color = "green"

# Number buttons
button1 = Button(root, text='1', fg='black', bg=num_color, command=lambda: press(1), height=3, width=6)
button1.grid(row=2, column=0)
button2 = Button(root, text='2', fg='black', bg=num_color, command=lambda: press(2), height=3, width=6)
button2.grid(row=2, column=1)
button3 = Button(root, text='3', fg='black', bg=num_color, command=lambda: press(3), height=3, width=6)
button3.grid(row=2, column=2)
button4 = Button(root, text='4', fg='black', bg=num_color, command=lambda: press(4), height=3, width=6)
button4.grid(row=3, column=0)
button5 = Button(root, text='5', fg='black', bg=num_color, command=lambda: press(5), height=3, width=6)
button5.grid(row=3, column=1)
button6 = Button(root, text='6', fg='black', bg=num_color, command=lambda: press(6), height=3, width=6)
button6.grid(row=3, column=2)
button7 = Button(root, text='7', fg='black', bg=num_color, command=lambda: press(7), height=3, width=6)
button7.grid(row=4, column=0)
button8 = Button(root, text='8', fg='black', bg=num_color, command=lambda: press(8), height=3, width=6)
button8.grid(row=4, column=1)
button9 = Button(root, text='9', fg='black', bg=num_color, command=lambda: press(9), height=3, width=6)
button9.grid(row=4, column=2)
button0 = Button(root, text='0', fg='black', bg=num_color, command=lambda: press(0), height=3, width=6)
button0.grid(row=5, column=1)

# Operator buttons
add = Button(root, text='+', fg='black', bg=op_color, command=lambda: press("+"), height=3, width=6)
add.grid(row=2, column=3)
sub = Button(root, text='-', fg='black', bg=op_color, command=lambda: press("-"), height=3, width=6)
sub.grid(row=3, column=3)
mult = Button(root, text='*', fg='black', bg=op_color, command=lambda: press("*"), height=3, width=6)
mult.grid(row=4, column=3)
div = Button(root, text='/', fg='black', bg=op_color, command=lambda: press("/"), height=3, width=6)
div.grid(row=5, column=3)

# Clear and Equal buttons
clear_button = Button(root, text='C', fg='white', bg=clear_color, command=clear, height=3, width=6)
clear_button.grid(row=5, column=0)
equal = Button(root, text='=', fg='white', bg=equal_color, command=equalpress, height=3, width=6)
equal.grid(row=5, column=2)

root.mainloop()
