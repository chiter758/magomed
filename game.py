import turtle


window = turtle.Screen()
window.title("Ping Pong By A L I")               
window.bgcolor("black")                                 
window.setup(width=800, height=600)                    
window.tracer(0)                                       


player1 = turtle.Turtle()
player1.speed(0) 
player1.shape("square")                         
player1.shapesize(stretch_wid=5, stretch_len=1)  
player1.color("yellow")                       
player1.penup()                                     
player1.goto(-370, 0)                           



player2 = turtle.Turtle()
player2.speed(0)                      
player2.shape("square")    
player2.shapesize(stretch_wid=5, stretch_len=1)     
player2.color("red")                           
player2.penup()                                
player2.goto(370, 0)                       

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)   
ball.dx = 0.5
ball.dy = 0.5


score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("player 1: 0 || player 2: 0", align = "center", font = ("Courier", 15, "normal"))

def player1_up():
    y = player1.ycor()
    y += 30
    player1.sety(y)

def player1_down():
    y = player1.ycor()
    y -= 30
    player1.sety(y)

def player2_up():
    y = player2.ycor()
    y += 30
    player2.sety(y)

def player2_down():
    y = player2.ycor()
    y -= 30
    player2.sety(y)



window.listen()
window.onkeypress(player1_up, "w")
window.onkeypress(player1_down, "s")
window.onkeypress(player2_up, "Up")
window.onkeypress(player2_down, "Down")


while True:

    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:

        ball.sety(290)
        ball.dy *= -1


    if ball.ycor() < -290:

        ball.sety(-290)
        ball.dy *= -1


    if ball.xcor() > 390:

        ball.goto(0, 0)
        ball.dx *= -1

        score1 += 1
        score.clear()
        score.write(f"player 1: {score1} || player 2: {score2}", align = "center", font = ("Courier", 15, "normal"))


    if ball.xcor() < -390:

        ball.goto(0, 0)
        ball.dx *= -1

        score2 += 1
        score.clear()
        score.write(f"player 1: {score1} || player 2: {score2}", align = "center", font = ("Courier", 15, "normal"))



    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player1.ycor() + 40 and ball.ycor() > player1.ycor() - 40):

        ball.setx(-340)
        ball.dx *=-1


   
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player2.ycor() + 40 and ball.ycor() > player2.ycor() - 40):

        ball.setx(340)
        ball.dx *=-1