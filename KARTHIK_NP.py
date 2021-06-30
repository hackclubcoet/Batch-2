# KARTHIK NP-2-TO DRAW A CHESS BOARD(8*8 SQUARE BOXES)
import turtle
a = turtle.Turtle()
for i in range(8):  # TO REPEATEDLY DRAW THE ROW FORMED INITIALLY 8 TIMES SO THAT A 8*8 SQUARE BOXES ARE FORMED
	a.penup()
	a.goto(0, -(i * 50))
	a.pendown()
	for j in range(8):  # TO REPEAT OR DRAW THE SQUARES 8 TIMES SO THAT 1ST ROW IS FORMED
		a.speed(20)  # TO SET SPEED OF DRAWING
		for k in range(5):  # TO DRAW 1ST SQUARE
			a.fd(50)
			if k != 4:
				a.rt(90)
