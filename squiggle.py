#squiggly + doodle = squiggle

import tkinter as tk
from tkinter import colorchooser

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SquigglyPaint v0.2")

        self.bg_color = "white"
        
        self.canvas = tk.Canvas(root, bg=self.bg_color, width=1080, height=720)
        self.canvas.pack()
        
        self.color = "black"
        self.brush_size = 3
        
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<Button-1>", self.paint)
        self.canvas.bind("<Shift-Button-1>", self.start_line)
        self.canvas.bind("<Shift-ButtonRelease-1>", self.end_line)
        
        self.controls_frame = tk.Frame(root)
        self.controls_frame.pack()
        
        self.clear_button = tk.Button(self.controls_frame, text="Clear", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT)
        
        self.brush_color_button = tk.Button(self.controls_frame, text="Choose Brush Color", command=self.choose_brush_color)
        self.brush_color_button.pack(side=tk.LEFT)

        self.bg_color_button = tk.Button(self.controls_frame, text="Choose Background Color", command=self.change_bg_color)
        self.bg_color_button.pack(side=tk.LEFT)
        
        self.size_slider = tk.Scale(self.controls_frame, from_=1, to=50, orient=tk.HORIZONTAL, label="Brush Size", command=self.change_brush_size)
        self.size_slider.set(self.brush_size)
        self.size_slider.pack(side=tk.LEFT) 

    def paint(self, event):
        x1, y1 = (event.x - self.brush_size/2), (event.y - self.brush_size/2)
        x2, y2 = (event.x + self.brush_size/2), (event.y + self.brush_size/2)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

    def clear_canvas(self):
        self.canvas.delete("all")

    def choose_brush_color(self):
        self.color = colorchooser.askcolor(color=self.color)[1]

    def change_brush_size(self, size):
        self.brush_size = int(size)

    def change_bg_color(self):
        self.bg_color = colorchooser.askcolor(color=self.bg_color)[1]
        self.canvas.config(bg=self.bg_color)

    def start_line(self,event):
        self.linex1, self.liney1 = (event.x), (event.y)

    def end_line(self,event):
        x2, y2 = (event.x), (event.y)
        self.canvas.create_line(self.linex1,self.liney1,x2,y2,width=self.brush_size,fill=self.color)

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()


'''Upcoming changes: 
                     2. Draw line (smooth lines button)
                     3. Undo - Redo Button
                     ~. Squiggly Animation on everything
                     ~. Host on netlify, vercel
                     4. Layers
                     5. Import Image
                     '''