import turtle

myturtle = turtle.Turtle()
myWindow = turtle.Screen()

def drawTurtle(my_turtle,line_length):
    if line_length > 0:
        my_turtle.right(45)
        my_turtle.forward(line_length)
        drawTurtle(my_turtle,line_length - 5)

        #drawTurtle(myturtle, line_length- 2)


#drawTurtle(myturtle, 100)
#myWindow.exitonclick()

def drawATurtle(my_turtle, line_length):
    my_turtle.right(90)
    my_turtle.forward(line_length)
    my_turtle.right(135)
    my_turtle.backward(line_length)
    my_turtle.forward(line_length)
    my_turtle.left(45)
    my_turtle.forward(line_length)


#drawATurtle(myturtle, 45)
#myWindow.exitonclick()


def tree(branch_len, t):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        print("inside one")
        tree(branch_len - 15, t)
        t.left(40)
        print("inside two")
        tree(branch_len - 15, t)
        t.right(20)
        t.backward(branch_len)
def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t)
    my_win.exitonclick()
main()

