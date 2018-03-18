from tkinter import *
from tkinter.ttk import *
import turtleFigures
from turtle import *

# contruct the Tk window
root = Tk()
root.geometry("600x150+300+300")
root.title("Turtle Fractals")
root.configure(background='#ECECEC')

mBar = Frame(root)
mBar.grid(row = 1, column = 2, columnspan = 12, padx = 5, pady = 5)


# contruct pen and screen
pen = Pen()
screen = Screen()
pen.color("black")
pen.speed(0.1)
pen.width(2)
screen.bgcolor("pink")

# define handlers

def onClear():
    # reset the entry-s
    orderStr.set("")
    lengthStr.set("")
    
    # reset the screen
    pen.reset()
    pen.speed(0.1)
    pen.width(2)
# end onClear

def onTree():
    # give the information about the figure
    infoLabel.config(text="This is a binary tree.")
    
    # get the order and length
    order = int(orderStr.get())
    length = int(lengthStr.get())

    # get a better initial position
    pen.up();pen.setx(-200);pen.down()

    # draw the figure
    turtleFigures.tree(order, length, pen)
    
#end onTree

def onTree4():
    # give the information about the figure
    infoLabel.config(text = "This constructs a quad tree with 4 similar branches symmetrically positioned.")
    
    # get the order and length
    order = int(orderStr.get())
    length = int(lengthStr.get())

    # get a better initial position
    pen.up();pen.setx(-200);pen.down()

    # draw the figure
    turtleFigures.tree4(order, length, pen)
    
#end onTree4

def onTree6():
    # give the information about the figure
    infoLabel.config(text = "This constructs a quad tree with 4 similar branches symmetrically positioned.")
    
    # get the order and length
    order = int(orderStr.get())
    length = int(lengthStr.get())

    # get a better initial position
    pen.up();pen.setx(-200);pen.down()

    # draw the figure
    turtleFigures.tree6(order, length, pen)
    
#end onTree6

def onFern():
    # give the information about the figure
    infoLabel.config(text = "This constructs a fern with 3 branches angled with 45, 30, 10 degree.")

    # get the order and length
    order = int(orderStr.get())
    length = int(lengthStr.get())

    # get a better initial position
    pen.up();pen.setx(-200);pen.down()

    # draw the figure
    turtleFigures.fern(order, length, pen)
    
#end onFern

def onFern2():
    # give the information about the figure
    infoLabel.config(text = "This constructs a fern with 3 branches angled with 45, 30, 10 degree.(with leaves)")
    
    # get the order and length
    order = int(orderStr.get())
    length = int(lengthStr.get())

    # get a better initial position
    pen.up();pen.setx(-200);pen.down()

    # draw the figure
    turtleFigures.fern2(order, length, pen)
    
#end onFern2

def onGasket():
    # give the information about the figure
    infoLabel.config(text = "This is to draw the sierpinsky gasket on equilateral triangle.")
    
    # get the order and length
    order = int(orderStr.get())
    length = int(lengthStr.get())

    # get a better initial position
    pen.up();pen.setx(-100);pen.sety(-100);pen.down()

    # draw the figure
    turtleFigures.gasket(order, length, pen)
    
#end onGasket

def onGasketRectangle():
    # give the information about the figure
    infoLabel.config(text = "This is to draw the sierpinsky gasket on equilateral rectangle.")
    
    # get the order and length
    order = int(orderStr.get())
    length = int(lengthStr.get())

    # get a better initial position
    pen.up();pen.setx(-100);pen.sety(-100);pen.down()

    # draw the figure
    turtleFigures.gasketRectangle(order, length, pen)
    
#end onGasketRectangle

def onGasketHexagon():
    # give the information about the figure
    infoLabel.config(text = "This is to draw the sierpinsky gasket on equilateral hexagon.")
    
    # get the order and length
    order = int(orderStr.get())
    length = int(lengthStr.get())

    # get a better initial position
    pen.up();pen.setx(-100);pen.sety(-100);pen.down()

    # draw the figure
    turtleFigures.gasketHexagon(order, length, pen)
    
#end onGasketHexagon

def onGasketCircle():
    # give the information about the figure
    infoLabel.config(text = "This is to draw the sierpinsky gasket on circle (4 circles).")
    
    # get the order and length
    order = int(orderStr.get())
    length = int(lengthStr.get())

    # get a better initial position
    pen.up();pen.sety(-200);pen.down()

    # draw the figure
    turtleFigures.gasketCircle(order, length, pen)
    
#end onGasketCircle

def onGasketCircle2():
    # give the information about the figure
    infoLabel = Label(root, text = "This is to draw the sierpinsky gasket on circle (6 circles).")
    infoLabel.grid(row = 3, column = 1, columnspan = 12, pady = 5)
    
    # get the order and length
    order = int(orderStr.get())
    length = int(lengthStr.get())

    # get a better initial position
    pen.up();pen.sety(-200);pen.down()

    # draw the figure
    turtleFigures.gasketCircle2(order, length, pen)
    
#end onGasketCircle2

def onFlake():
    # give the information about the figure
    infoLabel.config(text = "This is the loop of function koch to form a flake shape.")
    
    # get the order and length
    order = int(orderStr.get())
    length = int(lengthStr.get())

    # get a better initial position
    pen.up();pen.setx(-100);pen.sety(100);pen.down()

    # draw the figure
    turtleFigures.flake(order, length, pen)
    
#end onFlake

def onFlake2():
    # give the information about the figure
    infoLabel.config(text = "This is the loop of function koch to form a square flake shape.")
    
    # get the order and length
    order = int(orderStr.get())
    length = int(lengthStr.get())

    # get a better initial position
    pen.up();pen.setx(-100);pen.sety(100);pen.down()

    # draw the figure
    turtleFigures.flake2(order, length, pen)
    
#end onFlake2

def onSierpinski():
    # give the information about the figure
    infoLabel.config(text = "This sierpinski curve looks like a square.")
    
    # get the order and length
    order = int(orderStr.get())
    length = int(lengthStr.get())

    # get a better initial position
    pen.up();pen.setx(-200);pen.sety(-200);pen.down()

    # draw the figure
    turtleFigures.sierpinski(order, length, pen)
    
#end onSierpinski

def onSierpinski2():
    # give the information about the figure
    infoLabel.config(text = "This sierpinski looks like a square.")
    
    # get the order and length
    order = int(orderStr.get())
    length = int(lengthStr.get())

    # get a better initial position
    pen.up();pen.setx(-100);pen.sety(-200);pen.down()

    # draw the figure
    turtleFigures.sierpinski2(order, length, pen)
    
#end onSierpinski2



# make the interface

# add all components
titleLabel = Label(root, text = "Turtle Interface", font = ('Helvetica','16'))
titleLabel.grid(row = 0, column = 1, columnspan = 6, pady = 5)

orderLabel = Label(root, text = "Order")
orderLabel.grid(row = 1, column = 0,  padx = 10, pady = 5)
          
lengthLabel = Label(root, text = "Length")
lengthLabel.grid(row = 2, column = 0,  padx = 10, pady = 5)

orderStr = StringVar()
orderEntry = Entry(root, width = 18, textvariable = orderStr)
orderEntry.grid(row = 1, column = 1,  padx = 5, pady = 5)

lengthStr = StringVar()
lengthEntry = Entry(root, width = 18, textvariable = lengthStr)
lengthEntry.grid(row = 2, column = 1,  padx = 5, pady = 5)

def cascadeMenu():
    CasBtn = Menubutton(mBar, width = 12, text='Draw')
    CasBtn.grid(row = 1, column = 2, columnspan = 12)
    CasBtn.menu = Menu(CasBtn)
    CasBtn.menu.choices1 = Menu(CasBtn.menu)
    CasBtn.menu.choices2 = Menu(CasBtn.menu)
    CasBtn.menu.choices3 = Menu(CasBtn.menu)
    CasBtn.menu.choices4 = Menu(CasBtn.menu)
    CasBtn.menu.choices5 = Menu(CasBtn.menu)
    
    CasBtn.menu.choices1.add_command(label='Tree', underline=0, command=onTree)
    CasBtn.menu.choices1.add_command(label='Tree 4', underline=0, command=onTree4)
    CasBtn.menu.choices1.add_command(label='Tree 6', underline=0, command=onTree6)

    CasBtn.menu.choices2.add_command(label='Fern', underline=0, command=onFern)
    CasBtn.menu.choices2.add_command(label='Fern with leaves', underline=0, command=onFern2)

    CasBtn.menu.choices3.add_command(label='Gasket Triangle', underline=0, command=onGasket)
    CasBtn.menu.choices3.add_command(label='Gasket Rectangle', underline=0, command=onGasketRectangle)
    CasBtn.menu.choices3.add_command(label='Gasket Hexagon', underline=0, command=onGasketHexagon)
    CasBtn.menu.choices3.add_command(label='Gasket Circle 4', underline=0, command=onGasketCircle)
    CasBtn.menu.choices3.add_command(label='Gasket Circle 6', underline=0, command=onGasketCircle2)

    CasBtn.menu.choices4.add_command(label='Flake Triangle', underline=0, command=onFlake)
    CasBtn.menu.choices4.add_command(label='Flake Rectangle', underline=0, command=onFlake2)

    CasBtn.menu.choices5.add_command(label='Sierpinski Curve', underline=0, command=onSierpinski)
    CasBtn.menu.choices5.add_command(label='Sierpinski Hexagon', underline=0, command=onSierpinski2)
    
    CasBtn.menu.add_cascade(label='Tree', menu=CasBtn.menu.choices1)
    CasBtn.menu.add_cascade(label='Fern', menu=CasBtn.menu.choices2)
    CasBtn.menu.add_cascade(label='Gasket', menu=CasBtn.menu.choices3)
    CasBtn.menu.add_cascade(label='Flake', menu=CasBtn.menu.choices4)
    CasBtn.menu.add_cascade(label='Sierpinski', menu=CasBtn.menu.choices5)
    
    CasBtn['menu'] = CasBtn.menu
    return CasBtn

clearButton = Button(root, width = 12, text = "Clear", command = onClear)
clearButton.grid(row = 2, column = 2, columnspan = 12, padx = 5, pady = 5)

infoLabel = Label(root, text = "Info")
infoLabel.grid(row = 3, column = 0,  padx = 10, pady = 5)
infoLabel = Label(root, text = "Here is the infomation about the figure.")
infoLabel.grid(row = 3, column = 1, columnspan = 12, pady = 5)

CasBtn = cascadeMenu()
mBar.tk_menuBar(CasBtn)

mainloop()  

