from fractree import *
import tkinter as tk
import treeconfig
from PIL import Image, ImageTk
import threading as thread
import tkmacosx as tkmac
from export import Export as export


class Button(tk.Label):
    def __init__(self, parent, text, row, column, *args, **kwargs):
        tk.Label.__init__(self, parent, text=text, bg='#000000', fg='#ffffff', font=(
            'Raleway', 12), highlightcolor='#fff', activebackground='#000000', highlightthickness=1, borderwidth=2, relief="ridge", padx=10, pady=5,  * args, **kwargs)
        self.grid(row=row, column=column)

        self.bind('<Button-1>', self.press_change_color)
        self.bind('<ButtonRelease-1>', self.release_change_color)

    def press_change_color(self, event):
        self.config(bg="#fff", fg="#000", relief="sunken")

    def release_change_color(self, event):
        self.config(bg="#000", fg="#fff", relief="ridge")


class Logo(tk.Label):

    def __init__(self, parent, image, row, column, *args, **kwargs):
        self.image_object = Image.open(image)
        self.image_object = self.image_object.resize(
            (20, 20), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.image_object)
        tk.Label.__init__(self, parent, image=self.image,
                          bg="#000000", *args, **kwargs)

        self.grid(row=row, column=column, padx=5)


class Label(tk.Label):
    def __init__(self, parent, text, row, column, *args, **kwargs):
        tk.Label.__init__(self, parent, text=text, bg='#000000',
                          fg='#FFFFFF', font=("Raleway", 12),  *args, **kwargs)
        self.grid(row=row, column=column, sticky="W", padx=(0, 10))


class Input(tk.Entry):
    def __init__(self, parent, row, column, *args, **kwargs):
        tk.Entry.__init__(self, parent, bg='#000000', fg='#FFFFFF',
                          insertbackground='#FFFFFF', justify='center', width=7, borderwidth=1, highlightthickness=1, *args, **kwargs)
        self.grid(row=row, column=column)


class UI:

    def __init__(self, parent, *args, **kwargs):
        self.treeconfig = treeconfig.TreeConfig()
        # tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.tree = []

        height = root.winfo_screenheight()
        width = root.winfo_screenwidth()

        frame = tk.Frame(root, bg='#80c1ff')
        frame.place(relx=0, rely=0.0, relwidth=1, relheigh=1)

        self.w = tk.Canvas(frame, width=width, height=height, bg='#e8efef')
        self.w.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.88)

        label = tk.Label(frame, bg='#000000')
        label.place(relx=0, rely=0.88, relwidth=1, relheigh=0.12)

        form = tk.Frame(label, bg='#000000', padx=5, pady=10)
        form.place(relx=0.0, rely=0.0, relwidth=0.5, relheigh=1)

        form2 = tk.Frame(label, bg="#000000", padx=5, pady=10)
        form2.place(relx=0.65, rely=0.0, relwidth=0.5, relheight=1)

        def activateCheck():
            if self.treeconfig.slow_drawing == True:  # whenever checked
                self.treeconfig.slow_drawing = False
            elif self.treeconfig.slow_drawing == False:  # whenever unchecked
                self.treeconfig.slow_drawing = True

        Logo(form, image="assets/angle_module.png", row=0, column=1)
        Logo(form, image="assets/levels.png", row=1, column=1)
        Logo(form, image="assets/start_height.png", row=2, column=1)
        Logo(form, image="assets/dice.png", row=0, column=4)
        Logo(form, image="assets/trees.png", row=2, column=4)
        Logo(form, image="assets/width.png", row=1, column=4)
        Logo(form, image="assets/slow.png", row=0, column=7)

        Label(form, text="Angle Module", row=0, column=2)
        Label(form, text="Levels", row=1, column=2)
        Label(form, text="Length", row=2, column=2)
        Label(form, text="Angle Random Factor", row=0, column=5)
        Label(form, text="Width", row=1, column=5)
        Label(form, text="Number of Trees", row=2, column=5)
        Label(form, text="Slow Drawing", row=0, column=8)

        self.e1 = Input(form, row=0, column=3)
        self.e2 = Input(form, row=1, column=3)
        self.e3 = Input(form, row=2, column=3)
        self.e4 = Input(form, row=0, column=6)
        self.e5 = Input(form, row=1, column=6)
        self.e6 = Input(form, row=2, column=6)

        self.e7 = tk.Checkbutton(form, state='normal', bg='#000000', fg='#FFFFFF', justify='center',
                                 variable=self.treeconfig.slow_drawing, command=activateCheck, onvalue=True, offvalue=False)
        self.e7.grid(row=0, column=9)

        export_svg_button = Button(
            form2, text="Export to SVG", row=9, column=0)

        export_svg_button.bind('<Button-1>', self.export_to_svg)

        start = tk.Label(label, bg='#000000', bd=0,
                         text="GENERATE", fg='#FFFFFF', font=('Montserrat', 40), highlightcolor='#000000', activebackground='#000000')
        start.place(relx=0.375, rely=00, relwidth=0.25, relheigh=1)

        start.bind("<Button-1>", self.generate_tree)

        self.w.pack()

    def export_to_svg(self, event):
        export.svg(self, tree=self.tree)
        print("Tree exported!")

    def generate_tree(self, event):
        print('Start')
        self.w.delete("all")
        self.treeconfig.angle_module = int(
            self.e1.get() if self.e1.get() != "" else self.treeconfig.angle_module)
        self.treeconfig.levels = int(
            self.e2.get() if self.e2.get() != "" else self.treeconfig.levels)
        self.treeconfig.d = int(self.e3.get()) * - \
            1 if self.e3.get() != "" else self.treeconfig.d
        self.treeconfig.random_range = int(
            self.e4.get() if self.e4.get() != "" else self.treeconfig.random_range)
        self.treeconfig.width = int(
            self.e5.get()) * 0.01 if self.e5.get() != "" else self.treeconfig.width
        self.treeconfig.tree_number = int(
            self.e6.get() if self.e6.get() != "" else self.treeconfig.tree_number)
        # self.treeconfig.slow_drawing = bool(self.e7.get() if self.e6.get() != "" else self.treeconfig.tree_number)

        self.tree_cache = self.treeconfig.tree_cache
        fractree = Fractree(self.w, self.treeconfig)
        fractree.start(self.treeconfig.tree_number)
        print("Finished")
        self.tree = fractree.tree


if __name__ == "__main__":
    root = tk.Tk()
    root.state('zoomed')
    height = root.winfo_screenheight()
    width = root.winfo_screenwidth()

    root.title("Fractree")
    root.geometry(f'{width}x{height}')
    root.resizable(height=None, width=None)
    UI(root)
    root.mainloop()
