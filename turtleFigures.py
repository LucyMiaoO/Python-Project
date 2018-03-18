from turtle import *
import math


def tree(n, l, pen):
     if n == 0 or l < 2 :
          return
     #endif
     pen.forward(l)
     pen.left(45)
     tree(n-1, l/2, pen)
     pen.right(90)
     tree(n-1, l/2, pen)
     pen.left(45)
     pen.backward(l)
# end tree

def tree4(n, l, pen):
     '''
     tree4 constructs a quad tree with 4 similar branches symmetrically positioned.
     '''
     if n == 0 or l < 2 :
          return
     #endif
     pen.forward(l)
     pen.left(90)
     tree4(n-1, l/2, pen)
     pen.right(60)
     tree4(n-1, l/2, pen)
     pen.right(60)
     tree4(n-1, l/2, pen)
     pen.right(60)
     tree4(n-1, l/2, pen)
     pen.left(90)
     pen.backward(l)
# end tree4

def tree6(n, l, pen):
     '''
     tree6 constructs a quad tree with 6 similar branches symmetrically positioned.
     '''
     if n == 0 or l < 2 :
          return
     #endif
     pen.forward(l)
     pen.left(100)
     for i in range(5):
          tree6(n-1, l/3, pen)
          pen.right(40)
 
     tree6(n-1, l/3, pen)
     pen.left(100)
     pen.backward(l)
# end tree6

def fern(n, l, pen):
     '''
     this constructs a fern with 3 branches angled with 45, 30, 10 degree.
     '''
     if n == 0 or l < 2:
          return
     #endif
     pen.forward(0.3*l)
     pen.right(45);fern(n-1, l/2, pen);pen.left(45)
     pen.forward(0.7*l)
     pen.left(30);fern(n-1, l/2, pen);pen.right(30)
     pen.forward(l)
     pen.right(10);fern(n-1, 0.75*l, pen);pen.left(10)
     pen.backward(2*l)
# end fern

def fern2(n, l, pen):
     '''
     this constructs a fern with 3 branches angled with 45, 30, 10 degree.(with leaves)
     '''
     if n == 0 or l < 2:
          return
     #endif
     pen.forward(0.3*l)
     pen.right(45);fern2(n-1, l/2, pen);pen.left(45)
     pen.forward(0.7*l);pen.circle(l/4,90);pen.left(90);pen.circle(l/4,90);pen.left(90)
     pen.left(30);fern2(n-1, l/2, pen);pen.right(30)
     pen.forward(l);
     pen.right(10);fern2(n-1, 0.75*l, pen);pen.left(10);pen.circle(l/3,90);pen.left(90);pen.circle(l/3,90);pen.left(90)
     pen.backward(2*l)
# end fern2

def gasket(n, l, pen):
     '''
     gasket to draw the sierpinsky gasket on equilateral triangle.
     '''
     if n == 0 or l < 2 :
          for i in range(3):
               pen.forward(l);pen.left(120)
          #endfor
          return
     #endif
     for i in range(3):
          gasket(n-1, l/2, pen);pen.forward(l);pen.left(120)
     #endfor
# end gasket

def gasketRectangle(n, l, pen):
     '''
     gasketRectangle to draw the sierpinsky gasket on equilateral rectangle.
     '''
     if n == 0 or l < 2 :
          for i in range(4):
               pen.forward(l);pen.left(90)
          #endfor
          return
     #endif
     for i in range(4):
          gasketRectangle(n-1, l/3, pen);pen.forward(l);pen.left(90)
     #endfor
# end gasketRectangle

def gasketHexagon(n, l, pen):
     '''
     gasketHexagon to draw the sierpinsky gasket on equilateral hexagon.
     '''
     if n == 0 or l < 2 :
          for i in range(6):
               pen.forward(l);pen.left(60)
          #endfor
          return
     #endif
     for i in range(6):
          gasketHexagon(n-1, l/3, pen);pen.forward(l);pen.left(60)
     #endfor
# end gasketHexagon

def gasketCircle(n, l, pen):
     '''
     gasketCircle to draw the sierpinsky gasket on circle (4 circles).
     '''
     if n == 0 or l < 2 :
          for i in range(4):
               pen.circle(l,90)
          #endfor
          return
     #endif
     for i in range(4):
          gasketCircle(n-1, l/3, pen);pen.circle(l,90)
     #endfor
# end gasketCircle

def gasketCircle2(n, l, pen):
     '''
     gasketCircle2 to draw the sierpinsky gasket on circle (6 circles).
     '''
     if n == 0 or l < 2 :
          for i in range(6):
               pen.circle(l,60)
          #endfor
          return
     #endif
     for i in range(6):
          gasketCircle2(n-1, l/3, pen);pen.circle(l,60)
     #endfor
# end gasketCircle2

def koch(n, l, pen):

     if n == 0 or l < 2 :
          pen.forward(l)
          return
     #endif
     koch(n-1, l/3, pen)
     pen.left(60)
     koch(n-1, l/3, pen)
     pen.right(120)
     koch(n-1, l/3, pen)
     pen.left(60)
     koch(n-1, l/3, pen)
# end koch

def flake(n, l, pen):
     '''
     this is the loop of function koch to form a flake shape.
     '''
     for i in range(3):
          koch(n,l, pen);pen.right(120)
     #endfor
# end flake

def koch2(n, l, pen):

     if n == 0 or l < 2 :
          pen.forward(l)
          return
     #endif
     koch2(n-1, l/3, pen)
     pen.left(90)
     koch2(n-1, l/3, pen)
     pen.right(90)
     koch2(n-1, l/3, pen)
     pen.right(90)
     koch2(n-1, l/3, pen)
     pen.left(90)
     koch2(n-1, l/3, pen)
     
# end koch2

def flake2(n, l, pen):
     '''
     this is the loop of function koch to form a square flake shape.
     '''
     for i in range(4):
          koch2(n, l, pen);pen.right(90)
     #endfor
# end flake2

def koch3(n, l, pen):

     if n == 0 or l < 2 :
          return
     #endif
     koch3(n-1, l, pen)
     pen.left(45);pen.forward(l);pen.left(45)
     koch3(n-1, l, pen)
     pen.right(90);pen.forward(l);pen.right(90)
     koch3(n-1, l, pen)
     pen.left(45);pen.forward(l);pen.left(45)
     koch3(n-1, l, pen)
# end koch3

def sierpinski(n, l, pen):
     '''
     this sierpinski looks like a square.
     '''
     for i in range(4):
          koch3(n, l, pen);pen.left(90)
     #endfor
# end sierpinski

def sierpinski2(n, l, pen):
     '''
     this sierpinski looks like a hexagon.
     '''
     for i in range(6):
          koch3(n, l, pen);pen.left(60)
     #endfor
# end sierpinski2



     
     

