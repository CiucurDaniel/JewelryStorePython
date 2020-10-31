import turtle

# desen patrat cu repetarea statement-urilor
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)

#ridicam creionul si ne mutam mai departe pentru a desena noul patrat
turtle.penup()
turtle.forward(100)
turtle.pendown()

# desen patrat cu for
for i in range(1,5):
    turtle.forward(50)
    turtle.left(90)

#ridicam creionul si ne mutam mai departe pentru a desena noul patrat
turtle.penup()
turtle.forward(100)
turtle.pendown()

# desen patrat cu while
i = 1
while( i < 5 ):
    turtle.forward(50)
    turtle.left(90)
    i=i+1

turtle.done()


