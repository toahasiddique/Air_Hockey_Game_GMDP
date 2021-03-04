def setup():
    size(400, 600)
    background(255)
    global speedX, speedY, X, Y, puckRadius, doneState 
    speedX = 0
    speedY = 0
    doneState = False
    X = 100
    Y = 100
    puckRadius = 25

def draw_table():
    fill(0, 220, 255)
    circle(200, 0, 150)
    fill(255, 0, 0)
    circle(200, 300, 100)
    fill(255, 255, 255)
    circle(200, 300, 90)
    fill(255, 0, 0)
    circle(200, 300, 10)
    rect(0, 300, 150, 2)
    rect(250, 300, 150, 2)    
    
def draw():
    global speedX, speedY, X, Y, puckRadius, doneState
    background(255)

    draw_table()

    if speedX == 0 and speedY == 0:
        X = mouseX
        Y = 580 - puckRadius
    fill(255, 0, 0)
    ellipse(X, Y, puckRadius * 2, puckRadius * 2)
    
    # Draw paddle
    fill(237, 131, 50)
    rect(mouseX - 50, 580, 100, 20)

    # Move puck
    X = X + speedX
    Y = Y + speedY

    # Bounce
    if X > 400 - puckRadius or X < puckRadius:
        speedX = -speedX
    if Y > 580 - puckRadius and not doneState:
        if X < mouseX + 50 and X > mouseX - 50:
            speedY = -speedY
        else:
            doneState = True
    if Y < puckRadius and not doneState:
        if X > 125 + puckRadius and X < 275 - puckRadius:
            doneState = True
        else:
            speedY = -speedY
    



def mousePressed():
    global speedX, speedY, doneState
    if speedX == 0 and speedY == 0:
        speedY = -2 + -random(10)
        print("speedY: ", speedY)
        speedX = 3 + random(10)
        print("speedX: ", speedX)
    elif doneState:
        speedY = 0
        speedX = 0
        doneState = False
    print("Pressed")
