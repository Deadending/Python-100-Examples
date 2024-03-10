from tkinter import *

if __name__ == '__main__':
    root = Tk()
    root.title('Rectangle')
    canvas = Canvas(root, width=400, height=400, bg='white')
    x0 = 263
    y0 = 263
    x1 = 275
    y1 = 275
    for i in range(19):
        canvas.create_rectangle(x0, y0, x1, y1)
        x0 -= 5
        y0 -= 5
        x1 += 5
        y1 += 5

    canvas.pack()
    root.mainloop()