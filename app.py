#PING PONG GAME
import turtle
import winsound

win = turtle.Screen()
win.title("Classic Ping Pong Game")
win.bgcolor("#808080")
win.setup(width=800,height=600)
win.tracer(0)

#SCORING SYSTEM
score_a = 0 
score_b = 0

#ADD PADDLES (A)
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#ADD PADDLES (B)
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)

#ADD BALL 
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

#PEN 
pen = turtle.Turtle()
#AMIMATION SPEED
pen.speed(0) 
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("PLAYER A: 0  PLAYER B: 0 ", align="center", font=("Courier", 24, "bold"))

#MOVE PADDLE_A UP
def paddle_a_up():
    y = paddle_a.ycor()
    y  += 20
    paddle_a.sety(y) 

#MOVE PADDLE_A DOWN 
def paddle_a_down():
    y = paddle_a.ycor()
    y  -= 20
    paddle_a.sety(y) 

    #MOVE PADDLE_B UP
def paddle_b_up():
    y = paddle_b.ycor()
    y  += 20
    paddle_b.sety(y) 

#MOVE PADDLE_B DOWN 
def paddle_b_down():
    y = paddle_b.ycor()
    y  -= 20
    paddle_b.sety(y)


#KEYBOARD BINDINGS PADDLE LEFT 
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")


#KEYBOARD BINDINGS PADDLE RIGHT
win.listen()
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")


#MAIN GAME LOOP 
while True:
    win.update()

#MOVE THE BALL
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

#LEFT PADDLE STAY ON SCREEN     

    if paddle_a.ycor() > 250:
        paddle_a.sety(250) 
    
    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)

#RIGHT PADDLE STAY ON SCREEN     

    if paddle_b.ycor() > 250:
        paddle_b.sety(250) 
    
    if paddle_b.ycor() < -250:
        paddle_b.sety(-250) 


#BORDERS   
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        
#BORDERS LEFT AND RIGHT
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("PLAYER A: {} PLAYER B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
        ball.goto(0,0)
        ball.dx *= -1



    if ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("PLAYER A: {} PLAYER B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
        ball.goto(0,0)
        ball.dx *= -1

        

    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
        winsound.PlaySound("paddle_bounce.wav", winsound.SND_ASYNC)
    
    if ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        winsound.PlaySound("paddle_bounce.wav", winsound.SND_ASYNC)



    




