import turtle as trtl


def draw_spiral(number_of_reps, number_of_vertex):
    size = 0
    for _ in range(number_of_reps):
        trtl.forward(size)
        trtl.left((360/number_of_vertex)+0.2)
        size += 0.3

def draw_square(size, angle):
    for _ in range (360/angle):
            for _ in range(3):
                trtl.forward(size)
                trtl.left(120)
            trtl.left(angle)

def draw_art(size,angle):
    for _ in range(360/angle):
        for _ in range(2):
            for _ in range(size):
                trtl.forward(40)
                trtl.left(60)
                trtl.forward(40)
                trtl.right(60)
            trtl.left(240)
        trtl.left(angle)

def draw_star(size, num_of_vertex):
    for _ in range(num_of_vertex):
        trtl.forward(size)
        trtl.right(180-360/(2*num_of_vertex))

def draw_art2():
    for _ in range(50):
        x=50
        for _ in range(7):
            trtl.forward(x)
            x -= 5
            trtl.left(75)
            trtl.forward(x)
            x -= 5
            trtl.right(75)
        trtl.right(90)
        for _ in range(7):
            trtl.forward(x)
            x += 5
            trtl.right(75)
            trtl.forward(x)
            x += 5
            trtl.left(75)
draw_art2()
trtl.done()
