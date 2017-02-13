import display

#given x0 < x1
def draw_line( screen, x0, y0, x1, y1, color ):
    x = x0
    y = y0
    b = x0-x1
    a = y1-y0
    d = 2*a + b
    while (x <= x1):
        display.plot(screen, color, x , y)
        if (d<0):
            y-=1
            d-=2*b
        x+=1
        d+=2*a
    display.save_extension(screen, "line2.png")
