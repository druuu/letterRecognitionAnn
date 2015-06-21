from Tkinter import *
from Tkinter import BOTH, W, NW, SUNKEN, TOP, X, FLAT, LEFT
import subprocess

from PIL import Image, ImageDraw

b1 = "up"
xold, yold = None, None
white = (255, 255, 255)
black = (0, 0, 0)
width = 400
height = 400
center = height/2

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("Layout Test")
        self.config(bg = '#F0F0F0')
        self.pack(fill = BOTH, expand = 1)

        self.canvas1 = Canvas(self, relief = FLAT, background = "#000000",
                                            width = 400, height = 400)
        self.canvas1.pack(side = TOP, anchor = NW, padx = 100, pady = 10)

        self.canvas1.bind("<Motion>", self.motion)
        self.canvas1.bind("<ButtonPress-1>", self.b1down)
        self.canvas1.bind("<ButtonRelease-1>", self.b1up)

        self.submit = Button(self, text = "Submit", command = self.submitImg)
        self.submit.configure(activebackground = "#33B5E5", relief = FLAT)
        self.submit.pack(side = LEFT)

        self.clearCanvas = Button(self, text = "Clear", command =
                self.clearCanvasFun)
        self.clearCanvas.configure(activebackground = "#33B5E0", relief = FLAT)
        self.clearCanvas.pack(side = LEFT)

        self.drawL = Label(self.canvas1, text='Draw a capital letter',
                fg='white', bg='black')
        self.drawL.configure(activebackground = "#33B5E5", relief = FLAT)
        labelWindow = self.canvas1.create_window(10, 10, anchor=NW,
                window=self.drawL)
        self.drawL.pack()
        self.canvas1.create_window(10, 10, anchor = NW, window=self.drawL)

        #add quit button
        button1 = Button(self, text = "Quit", command = self.quit, anchor = W)
        button1.configure(width = 10, activebackground = "#33B5E5", relief =
                FLAT)
        button1_window = self.canvas1.create_window(10, 10, anchor=NW,
                window=button1)
        button1.pack(side = LEFT)

        self.image1 = Image.new("RGB", (400, 400), black)
        self.draw = ImageDraw.Draw(self.image1)
        self.filename = "my_drawing.jpg"


    def b1up(self, event):
        global b1, xold, yold
        b1 = "up"
        xold = None           
        yold = None

    def b1down(self, event):
        global b1
        b1 = "down"

    def motion(self, event):
        if b1 == "down":
            global xold, yold
            if xold is not None and yold is not None:
                event.widget.create_line(xold ,yold ,event.x ,event.y,
                         width = 76, fill = 'white')
                self.draw.line([xold,yold,event.x,event.y], white, width = 76)
            xold = event.x
            yold = event.y

        self.canvas1.update()
        self.image1.save(self.filename)

    def clearCanvasFun(self):
        self.canvas1.delete('all')

    def submitImg(self):
        subprocess.call('./letRec.sh')
        alphaList = []
        alphaFile = open('result.txt', 'r')
        for line in alphaFile:
            line = line.replace('\n', '')
            alphaList.append(line)

        letters = '8ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        predAlpha = letters[int(alphaList[3])]
        self.drawL = Label(self, width = 20, height = 2, text= 'Predicted letter is: ' + predAlpha, fg='white', bg='black')
        self.drawL.configure(activebackground = "#33B5E5", relief = FLAT)
        self.drawL.pack(side = LEFT)




def main():
    root = Tk()
    root.geometry('500x500')
    app = Example(root)
    app.mainloop()

if __name__ == '__main__':
    main()
