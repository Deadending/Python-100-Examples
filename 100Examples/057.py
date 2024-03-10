from tkinter import *

if __name__ == '__main__':
    canvas = Canvas(width=300, height=300, bg='white')
    canvas.pack(expand=YES, fill=BOTH)
    x0 = 263
    y0 = 263
    x1 = 275
    y1 = 275
    for i in range(19):
        canvas.create_line(x0, y0, x0, y1, width=1, fill='black')
        x0 -= 5
        y0 -= 5
        x1 += 5
        y1 += 5

    mainloop()