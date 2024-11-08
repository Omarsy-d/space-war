import turtle
import random
import math

def main():
    #Screen
    main_screen = turtle.Screen()
    main_screen.bgcolor("black")
    main_screen.title("Space War")
    main_screen.tracer(0)
    main_screen.bgpic("C:/Users/Hp/OneDrive/mac book air back up one drive/Desktop/space war/background.gif")

    instructions_pen = turtle.Turtle()
    instructions_pen.speed(0)
    instructions_pen.color("white")
    instructions_pen.penup()
    instructions_pen.setposition(280, 220)
    instructions_pen.write("How to play:\nUse Arrow Keys to Move\nSpacebar to Shoot\nYou lose if the alien reaches the bottom", align="right", font=("arial", 12, "normal"))
    instructions_pen.hideturtle()

    #Border
    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.color("white")
    border_pen.penup()
    border_pen.setposition(-300, -300)
    border_pen.pendown()
    border_pen.pensize(3)

    for side in range(4):
        border_pen.fd(600)
        border_pen.left(90)

    border_pen.hideturtle()

    #Score
    global score
    score = 0
    score_pen = turtle.Turtle()
    score_pen.speed(0)
    score_pen.color("white")
    score_pen.penup()
    score_pen.setposition(-290, 280)
    scorestring = "Score: %s" % score
    score_pen.write(scorestring, False, align="left", font=("arial", 14, "normal"))
    score_pen.hideturtle()

    #register images
    main_screen.register_shape("C:/Users/Hp/OneDrive/mac book air back up one drive/Desktop/space war/invader2.gif")
    main_screen.register_shape("C:/Users/Hp/OneDrive/mac book air back up one drive/Desktop/space war/spaceship.gif")

    #Player
    player = turtle.Turtle()
    player.color("blue")
    player.shape("C:/Users/Hp/OneDrive/mac book air back up one drive/Desktop/space war/spaceship.gif")
    player.penup()
    player.speed(0)
    player.setposition(0, -270)
    player.setheading(90)
    player.move_speed = 15
    

    #Enemy
    number_of_enemies = 5
    enemies = []
    for i in range(number_of_enemies):
        enemy = turtle.Turtle()
        enemy.color("red")
        enemy.shape("C:/Users/Hp/OneDrive/mac book air back up one drive/Desktop/space war/invader2.gif")
        enemy.penup()
        enemy.speed(5)
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        enemy.setposition(x, y)
        enemies.append(enemy)

    enemyspeed = 1.5

    #Bullet looks
    bullet = turtle.Turtle()
    bullet.shape("triangle")
    bullet.color("yellow")
    bullet.penup()
    bullet.speed(0)
    bullet.shapesize(0.5, 0.5)
    bullet.setheading(90)
    bullet.hideturtle()

    bulletspeed = 20
    bulletstate = "ready"

    #Player left
    def move_left():
        x = player.xcor()
        x -= player.move_speed
        if x < -280:
            x = -280
        player.setx(x)
    
    #Player right
    def move_right():
        x = player.xcor()
        x += player.move_speed
        if x > 280:
            x = 280
        player.setx(x)

    #Bullet
    def fire_bullet():
        nonlocal bulletstate
        if bulletstate == "ready":
            bulletstate = "fire"
            x = player.xcor()
            y = player.ycor() + 10
            bullet.setposition(x, y)
            bullet.showturtle()

    #Collision
    def is_collision(t1, t2):
        distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
        return distance < 15 
    #Keybinds
    main_screen.listen()
    main_screen.onkey(move_left, "Left")
    main_screen.onkey(move_right, "Right")
    main_screen.onkey(fire_bullet, "space")

    #Game loop
    def game_loop():
        global score
        nonlocal bulletstate, enemyspeed

        #Enemy collison & movement
        for enemy in enemies:
            x = enemy.xcor()
            x += enemyspeed
            enemy.setx(x)

            #Checking for the borders
            if enemy.xcor() > 280 or enemy.xcor() < -280:
                for e in enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                enemyspeed *= -1

            if enemy.ycor() < -300:
                return

            #Checking collision with the bullet
            if is_collision(bullet, enemy):
                bullet.hideturtle()
                bulletstate = "ready"
                bullet.setposition(0, -400)
                x = random.randint(-200, 200)
                y = random.randint(100, 250)
                enemy.setposition(x, y)

                #1 dead enemy = 10 points
                score += 10
                scorestring = "Score: %s" % score
                score_pen.clear()
                score_pen.write(scorestring, False, align="left", font=("arial", 14, "normal"))

            #player gets bombed by enemy
            if is_collision(player, enemy):
                player.hideturtle()
                enemy.hideturtle()
                print("Game Over")
                return 

        #Bullet movement
        if bulletstate == "fire":
            y = bullet.ycor()
            y += bulletspeed
            bullet.sety(y)

            #Bullet top-border
            if bullet.ycor() > 275:
                bullet.hideturtle()
                bulletstate = "ready"

        #Repeat game loop
        main_screen.update()
        main_screen.ontimer(game_loop, 10)

    #Start game loop
    game_loop()
    main_screen.mainloop()

if __name__ == "__main__":
    main()
