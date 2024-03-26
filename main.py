from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
GAME_SPEED = 0.05

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Ssssnake Game")
my_screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(snake.up, "w")
my_screen.onkey(snake.down, "s")
my_screen.onkey(snake.left, "a")
my_screen.onkey(snake.right, "d")

is_running = True
while is_running:
    my_screen.update()
    time.sleep(GAME_SPEED)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.add_score()
        snake.extend_snake()

    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        scoreboard.game_over()
        is_running = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_running = False
            scoreboard.game_over()

my_screen.exitonclick()
