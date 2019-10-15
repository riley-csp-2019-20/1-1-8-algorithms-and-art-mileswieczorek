import turtle as trtl
cake = trtl.Turtle()

cake.hideturtle()
cake.pensize(4)
cake.pencolor("brown")
cake.speed(10)

# making the top rectangle of the cake
i = 0
while (i < 2):
    cake.fillcolor("brown")
    cake.begin_fill()
    cake.forward(200)
    cake.right(90)
    cake.forward(100)
    cake.right(90)
    cake.end_fill()
    i = (i + 1)

cake.penup()
cake.goto(0,-100)
cake.pendown()
cake.right(180)


# making the bottom rectangle of cake
c = 0
while (c < 2):
    cake.fillcolor("brown")
    cake.begin_fill()
    cake.forward(50)
    cake.left(90)
    cake.forward(100)
    cake.left(90)
    cake.forward(250)
    cake.end_fill()
    c+=1

# making the frosting for first rectangle
cake.penup()
cake.goto(200,0)
cake.pendown()

f = 0
while (f < 6):
    cake.fillcolor("red")
    cake.begin_fill()
    cake.circle(20)
    cake.end_fill()
    cake.up()
    cake.forward(40)
    cake.down()
    f += 1


# making frosting for second rectangle
cake.penup()
cake.goto(250,-100)
cake.pendown()

f = 0
while (f < 6):
    cake.fillcolor("red")
    cake.begin_fill()
    cake.circle(30)
    cake.end_fill()
    cake.up()
    cake.forward(60)
    cake.down()
    f+= 1


# making the candle
cake.penup()
cake.goto(100,0)
cake.pendown()

cake.pencolor("black")
cake.right(90)
cake.forward(40)



# making the flame move
while True:
    cake.goto(110,40)
    cake.fillcolor("red")
    cake.begin_fill()
    cake.circle(10)
    cake.end_fill()
    cake.goto(110,40)
    cake.fillcolor("yellow")
    cake.begin_fill()
    cake.circle(10)
    cake.end_fill()





wn = trtl.Screen()
wn.mainloop()








