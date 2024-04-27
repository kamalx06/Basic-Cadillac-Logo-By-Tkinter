from tkinter import *

form = Tk()
canvas = Canvas(form)

canvas.create_line(30,50,30,80,30, 47, 20, 30, 60, 20, 100, 30, 86,
                   47, 86, 78, 86, 80, 55, 90, 30, 80, 55, 90, 87, 80) #outside

canvas.create_rectangle(34, 45, 60, 48, fill=("#3E220D"))  # brown left
canvas.create_rectangle(60, 35, 72, 46, fill=("#E73A23"))  # red light
canvas.create_rectangle(72, 36, 82, 46, fill=("#E73A23"))  # red light right
canvas.create_rectangle(72, 35, 84, 40, fill=("#C3B0B0"))  # light gray right
canvas.create_rectangle(72, 41, 84, 46, fill=("#C3B0B0"))  # light gray right
canvas.create_rectangle(72, 39, 84, 42, fill=("blue"))  # blue right

canvas.create_rectangle(72, 46, 84, 56, fill=("#E73A23"))  # red light

canvas.create_rectangle(60, 45, 72, 50, fill=("#C3B0B0"))  # light gray right
canvas.create_rectangle(60, 51, 72, 56, fill=("#C3B0B0"))  # light gray right
canvas.create_rectangle(60, 49, 72, 52, fill=("blue"))  # blue right
canvas.create_rectangle(34, 56, 44, 65, fill=("#E73A23"))  # red light left
canvas.create_rectangle(44, 56, 60, 61, fill=("#C3B0B0"))  # light gray left
canvas.create_rectangle(44, 61, 60, 65, fill=("#C3B0B0"))  # light gray left
canvas.create_rectangle(44, 59, 60, 61, fill=("blue"))  # blue left
canvas.create_rectangle(60,61,84,66, fill=("#3E220D"))#brown right
canvas.create_rectangle(50, 65, 60, 75, fill=("#E73A23"))# red light left 2
canvas.create_rectangle(34, 65, 50, 71, fill=("#C3B0B0"))  # light gray left
canvas.create_rectangle(34, 71, 50, 75, fill=("#C3B0B0"))  # light gray left
canvas.create_rectangle(34, 69, 50, 71, fill=("blue"))  # blue left
canvas.create_rectangle(34, 48, 60, 56, fill=("#A58F16"))#gold left
canvas.create_rectangle(34, 35, 60, 45, fill=("#A58F16"))
canvas.create_rectangle(60, 56, 84, 61, fill=("#A58F16"))#gold right
canvas.create_rectangle(60, 66, 84, 75, fill=("#A58F16"))  # gold right
canvas.pack() #packet

form.mainloop()
