from turtle import *


class Sprite(Turtle):
    def __init__(self, x, y, step, colour, shapes):
        super().__init__()
        self.speed(10)
        self.color(colour)
        self.pu()
        self.goto(x, y)
        self.shape(shapes)
        self.step = step

    def move_right(self):
        self.goto((self.xcor() + self.step), self.ycor())

    def move_left(self):
        self.goto((self.xcor() - self.step), self.ycor())

    def move_up(self):
        self.goto((self.xcor(), self.ycor() + self.step))

    def move_down(self):
        self.goto((self.xcor(), self.ycor() - self.step))

    def is_collade(self, target, t1, t2, t3):
        while self.points != 12:
            dist = self.distance(target.xcor(), target.ycor())
            if dist < 30:
                self.points += 1
                if self.points == 2:
                    t3.st()
                score.clear()
                score.write(self.points, font=("Arial", 24, "bold"))
                t1.step *= 2
                t2.step *= 2
                t3.step *= 2
                self.goto(0, -150)
                self.is_collade(target, t1, t2, t3)
            else:
                return False

        score.clear()
        t1.ht()
        t2.ht()
        t3.ht()
        score.write("You win!!!", font=("Arial", 24, "bold"))
        return True


score = Sprite(-100, 200, 0, "green", "circle")
score.ht()
score.write(0, font=("Arial", 24, "bold"))
t4 = Sprite(0, 200, 10, "aqua", "circle")


class hide_and_sik(Sprite):
    def __init__(self, x, y, step, colour, shapes):
        super().__init__(x, y, step, colour, shapes)
        self.points = 0
        scr = self.getscreen()
        scr.listen()
        scr.onkey(self.move_right, "d")
        scr.onkey(self.move_left, "a")
        scr.onkey(self.move_up, "w")
        scr.onkey(self.move_down, "s")


t = hide_and_sik(0, -100, 10, "green", "turtle")


class Secure(Sprite):
    def __init__(self, x, y, step, colour, shapes):
        super().__init__(x, y, step, colour, shapes)

    def move_x(self):
        self.goto((self.xcor() + self.step), self.ycor())

    def move(self, selfer, t, t3, t4):
        w = 200
        while t.is_collade(t4, t2, t3, t1) == False:
            dist = self.distance(t.xcor(), t.ycor())
            if dist < 30:
                score.clear()
                t.goto(0, -150)
                score.color("red")
                score.write("You lose!!!", font=("Arial", 24, "bold"))
                t4.ht()
                break

            dist = self.distance(t2.xcor(), t2.ycor())
            if dist < 30:
                score.clear()
                t.goto(0, -150)
                score.color("red")
                t4.ht()
                score.write("You lose!!!", font=("Arial", 24, 'bold'))
                break

            dist = self.distance(t4.xcor(), t4.ycor())
            if dist < 30:
                score.clear()
                t.goto(0, -150)
                score.color("red")
                score.write("You lose!!!", font=("Arial", 24, "bold"))
                t4.ht()
                break

            self.move_x()
            selfer.move_x()
            t3.move_x()
            if self.xcor() >= w:
                self.step = -self.step
            if self.xcor() <= -w:
                self.step = -self.step

            if selfer.xcor() >= w:
                selfer.step = -selfer.step
            if selfer.xcor() <= -w:
                selfer.step = -selfer.step

            if t3.xcor() >= w:
                t3.step = -t3.step
            if t3.xcor() <= -w:
                t3.step = -t3.step


t1 = Secure(-100, 100, 10, "red", "square")
t2 = Secure(100, 150, 10, "red", "square")
t3 = Secure(0, 125, 10, "red", "square")

t1.move(t2, t, t3, t4)

exitonclick()

