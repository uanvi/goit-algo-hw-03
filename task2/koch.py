import turtle
import sys

def koch_snowflake(t, order, size):
    """Recursively draw a Koch Snowflake."""
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)

def main():
    if len(sys.argv) < 2:
        print("Usage: python koch.py <recursion_level>")
        sys.exit(1)

    try:
        order = int(sys.argv[1])
    except ValueError:
        print("Error: Recursion level must be an integer.")
        sys.exit(1)

    # Set up the turtle environment
    t = turtle.Turtle()
    t.speed(0)  
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("white")
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    # Draw the Koch alg
    for _ in range(3):
        koch_snowflake(t, order, 400)
        t.right(120)

    # Hide the turtle and display the window
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
