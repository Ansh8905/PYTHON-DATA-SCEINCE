import pgzrun

WIDTH = 900
HEIGHT = 700

p = Actor ('char2', (10, 200))
q = Actor ('char1', (200,200))
speed = 7

def draw ():
    screen.fill('yellow')
    p.draw()
    q.draw()

def update():
    player_controls()
    player_controls1()


def player_controls():
    if keyboard.UP and not  p.top < 0:
        p.y += -speed
        p.angle = 0
    elif keyboard.DOWN and  not p.bottom > HEIGHT:
        p.y += speed
        p.angle = 0
    elif keyboard.LEFT and not  p.left<0:
        p.x += -speed
        p.angle = 10
    elif keyboard.RIGHT and  not p.right > WIDTH:
        p.x += speed
        p.angle = -10

def player_controls1():
    if keyboard.W and not  q.top< 0:
        q.y += -speed
        q.angle = 10
    elif keyboard.S and  not q.bottom > HEIGHT:
        q.y += speed
        p.angle = 10
    elif keyboard.A and not  q.left<0:
        q.x += -speed
        q.angle = 20
    elif keyboard.D and  not q.right > WIDTH:
        q.x += speed
        q.angle = -20




pgzrun.go()


















