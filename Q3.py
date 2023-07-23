from tkinter import Tk, Canvas
frame=Tk()
canvas=Canvas(bg='black',height=500,width=300)

canvas.create_rectangle(50, 60, 240, 160, fill='red', outline='blue')

canvas.create_text(100, 100, text='Chu Cheong Ming', anchor='nw', font='TkMenuFont', fill='blue')

canvas.create_line(100,115,200,115)
'''
coord=(100, 100, 200, 200)
canvas.create_arc(coord,start=0,extent=90,fill='white')
canvas.create_arc(coord,start=90,extent=90,fill='blue')
canvas.create_arc(coord,start=180,extent=90,fill='white')
canvas.create_arc(coord,start=270,extent=90,fill='blue')
'''

canvas.pack()
frame.mainloop()

'''
canvas.create_rectangle(10, 10, 200, 50, fill='red', outline='blue')
canvas.create_text(100, 100, text='A wonderful story', anchor='nw', font='TkMenuFont', fill='red')
'''
