import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)

    elif letter == "A":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        tur.setpos(40, 0)
        tur.left(180)
    elif letter == "B":
	    pass
    elif letter == "C":
        tur.penup()
        tur.right(90)
        tur.forward(35)
        tur.right(90)
        tur.forward(20)
        tur.pendown()
        tur.left(210)
        tur.circle(15,270)
        tur.penup()
        tur.right(4)
        tur.forward(12)
        tur.left(60)
        tur.forward(35)
        tur.right(90)
    elif letter == "D":
	    pass
    elif letter == "E":
	tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.pd()
        tur.fd(40)
        tur.right(270)
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(20)
        tur.right(180)
        tur.fd(20)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(35)             
    elif letter == "F":
	    pass
    elif letter == "G":
	    pass		
    elif letter == "H":
	    pass
    elif letter == "I":
	    tur.pu() 
	    tur.fd(5)
	    tur.right(90)
	    tur.fd(10)
	    tur.left(90)
	    tur.pd()
	    tur.fd(30)
	    tur.pu()
	    tur.right(180)
	    tur.fd(15)
	    tur.left(90)
	    tur.pd()
	    tur.fd(40)
	    tur.pu()
	    tur.right(90)
	    tur.fd(15)
	    tur.right(180)
	    tur.pd()
	    tur.fd(30)
	    tur.pu()
	    tur.fd(5)
	    tur.left(90)
	    tur.fd(50)
	    tur.right(90)
    elif letter == "J":
	tur.pd()
        tur.forward(20)
        tur.left(180)
        tur.forward(10)
        tur.left(90)
        tur.forward(30)
        tur.left(180)
        tur.circle(5,-180)
        tur.left(180)
        tur.pu()
        tur.forward(35)
        tur.right(90)
        tur.forward(40) 
    elif letter == "K":
	    pass
    elif letter == "L":
	    pass
    elif letter == "M":
	    pass
    elif letter == "N":
	    pass
    elif letter == "O":
	    pass
    elif letter == "P":
            tur.setheading(0)
            tur.pu()
            tur.fd(5)
            tur.right(90)
            tur.fd(5)
            tur.pd()
            tur.forward(30)
            tur.right(180)
            tur.forward(30)
            tur.right(90)
            tur.circle(-10, 180)
            tur.pu()
            tur.right(180)
            tur.forward(35)
            tur.left(90)
            tur.forward(25)
            tur.right(90)
            tur.pd()
    elif letter == "Q":
	    pass
    elif letter == "R":
	    pass
    elif letter == "S":
	    pass
    elif letter == "T":
	tur.pd()
        tur.forward(20)
        tur.left(180)
        tur.forward(10)
        tur.left(90)
        tur.forward(30)
        tur.left(180)
        tur.pu()
        tur.forward(35)
        tur.right(90)
        tur.forward(30)
    elif letter == "U":
	    pass
    elif letter == "V":
            tur.setheading(0)
            tur.pu()
            tur.fd(5)
            tur.right(90)
            tur.fd(5)
            tur.pd()
            tur.left(30)
            tur.forward(30)
            tur.left(120)
            tur.forward(30)
            tur.pu()
            tur.forward(6) 
            tur.right(60)
            tur.forward(3)
            tur.pd()
    elif letter == "W":
	    pass
    elif letter == "X":
	    pass
    elif letter == "Y":
	    pass
    elif letter == "Z":
	    pass		

        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        turtleLetter("box",tur)
	







window = turtle.Screen()
tur = turtle.Turtle()
tur.speed(1)
turtleLetter("box",tur)
turtleLetter("P",tur)
turtleLetter("V",tur)



window.exitonclick()
