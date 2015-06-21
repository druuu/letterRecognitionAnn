from Tkinter import *
from PIL import Image, ImageDraw


b1 = "up"
xold, yold = None, None

white = (255, 255, 255)
black = (0, 0, 0)
width = 400
height = 400
center = height/2



def b1down(event):
    global b1
    b1 = "down"           

def b1up(event):
    global b1, xold, yold
    b1 = "up"
    xold = None           
    yold = None

def motion(event):
    if b1 == "down":
        global xold, yold
        if xold is not None and yold is not None:
            event.widget.create_line(xold,yold,event.x,event.y,smooth=TRUE)
            event.widget.create_line(xold ,yold ,event.x + 1,event.y +
                    1,smooth=TRUE, width = 25, fill = 'white')

            draw.line([xold,yold,event.x,event.y], white, width = 25)

                    
        xold = event.x
        yold = event.y

    drawing_area.update()
    image1.save(filename)


    

    
        

root = Tk()

root.title("letterRecognitio")

#root.drawLB = Button(root, text = "Draw", command = canvasFun)
#root.drawLB.grid()

root.drawL = Label(root, text = "Draw capital letter")
root.drawL.grid()

drawing_area = Canvas(root, width = width, height = height, bg = 'black')
drawing_area.pack()

image1 = Image.new("RGB", (400, 400), black)
draw = ImageDraw.Draw(image1)
filename = "my_drawing.jpg"


drawing_area.bind("<Motion>", motion)
drawing_area.bind("<ButtonPress-1>", b1down)
drawing_area.bind("<ButtonRelease-1>", b1up)

root.mainloop()


