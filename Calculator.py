from tkinter import *

root = Tk()
root.geometry("350x500+0+0")
root.title("Calculator")

text_Input = StringVar()
operator = ""

#========================functions======================#
def btnClick(numbers):
	global operator
	operator = operator + str(numbers)
	text_Input.set(operator)

def btnClearDisplay():
	global operator
	operator = ""
	text_Input.set("")

def btnEqualsInput():
	global operator
	sumup = str(eval(operator))
	text_Input.set(sumup)
	operator = " "
#==================Display===============================
txtDisplay = Entry(root, font=('arial',20,'bold'),textvariable=text_Input,bd=30,insertwidth=4,bg='light blue',justify='center')
txtDisplay.grid(columnspan=4)
operator = ""
#=====================Buttons=========================#
Button7 = Button(root, padx=14, pady=14,bd=8,fg="black",font=('arial',20,'bold'),text="7",bg="powder blue",command=lambda:btnClick(7)).grid(row=2, column=0)
Button8 = Button(root, padx=14, pady=14,bd=8,fg="black",font=('arial',20,'bold'),text="8",bg="powder blue",command=lambda:btnClick(8)).grid(row=2, column=1)
Button9 = Button(root, padx=14, pady=14,bd=8,fg="black",font=('arial',20,'bold'),text="9",bg="powder blue",command=lambda:btnClick(9)).grid(row=2, column=2)
ButtonAdd = Button(root, padx=14, pady=14,bd=8,fg="black",font=('arial',20,'bold'),text="+",bg="powder blue",command=lambda:btnClick('+')).grid(row=2, column=3)

Button4 = Button(root, padx=14, pady=14,bd=8,fg="black",font=('arial',20,'bold'),text="4",bg="powder blue",command=lambda:btnClick(4)).grid(row=3, column=0)
Button5 = Button(root, padx=14, pady=14,bd=8,fg="black",font=('arial',20,'bold'),text="5",bg="powder blue",command=lambda:btnClick(5)).grid(row=3, column=1)
Button6 = Button(root, padx=14, pady=14,bd=8,fg="black",font=('arial',20,'bold'),text="6",bg="powder blue",command=lambda:btnClick(6)).grid(row=3, column=2)
ButtonMin = Button(root, padx=14, pady=14,bd=8,fg="black",font=('arial',20,'bold'),text="-",bg="powder blue",command=lambda:btnClick('-')).grid(row=3, column=3)

Button1 = Button(root, padx=14, pady=14,bd=8,fg="black",font=('arial',20,'bold'),text="1",bg="powder blue",command=lambda:btnClick(1)).grid(row=4, column=0)
Button2 = Button(root, padx=14, pady=14,bd=8,fg="black",font=('arial',20,'bold'),text="2",bg="powder blue",command=lambda:btnClick(2)).grid(row=4, column=1)
Button3 = Button(root, padx=14, pady=14,bd=8,fg="black",font=('arial',20,'bold'),text="3",bg="powder blue",command=lambda:btnClick(3)).grid(row=4, column=2)
ButtonMult = Button(root, padx=14, pady=14,bd=8,fg="black",font=('arial',20,'bold'),text="*",bg="powder blue",command=lambda:btnClick('*')).grid(row=4, column=3)

Button0 = Button(root, padx=14, pady=14,bd=8,fg="black",font=('arial',20,'bold'),text="0",bg="powder blue",command=lambda:btnClick(0)).grid(row=5, column=0)
ButtonClear = Button(root, padx=14, pady=14,bd=8,fg="black",font=('arial',20,'bold'),text="c",bg="powder blue",command = btnClearDisplay).grid(row=5, column=1)
ButtonEqual = Button(root, padx=14, pady=14,bd=8,fg="black",font=('arial',20,'bold'),text="=",bg="powder blue",command = btnEqualsInput).grid(row=5, column=2)
ButtonDiv = Button(root, padx=14, pady=14,bd=8,fg="black",font=('arial',20,'bold'),text="/",bg="powder blue",command=lambda:btnClick('/')).grid(row=5, column=3)

root.mainloop()
