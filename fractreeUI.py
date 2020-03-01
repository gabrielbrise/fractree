from tkinter import *
from fractree import *
import treeconfig
from PIL import Image, ImageTk

class UI:

    def __init__(self, parent, *args, **kwargs):
        self.treeconfig = treeconfig.TreeConfig()
        # tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        root.state("zoomed")

        # height = root.winfo_screenheight()
        # width = root.winfo_screenwidth()
        height = 1080
        width = 1920

        frame = Frame(root, bg='#80c1ff')
        frame.place(relx=0, rely=0.0, relwidth=1, relheigh=1)

        self.w = Canvas(frame, width=width, height=height, bg='#e8efef')
        self.w.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.88)

        label = Label(frame, bg='#000000')
        label.place(relx=0, rely=0.88, relwidth=1, relheigh=0.12)

        form = Frame(label, bg='#000000', padx=5, pady=10)
        form.place(relx=0.0, rely=0.0, relwidth=0.5, relheigh=1)

        Label(form, text="Angle Module", bg='#000000', fg='#FFFFFF', font=("Montserrat", 10)).grid(row=0, column=2, sticky="W", padx=(0, 10))
        Label(form, text="Levels", bg='#000000', fg='#FFFFFF', font=("Montserrat", 10), anchor="w").grid(row=1, column=2, sticky="W", padx=(0, 10))
        Label(form, text="Length", bg='#000000', fg='#FFFFFF', font=("Montserrat", 10)).grid(row=2, column=2, sticky="W", padx=(0, 10))
        Label(form, text="Angle Random Factor", bg='#000000', fg='#FFFFFF', font=("Montserrat", 10)).grid(row=0, column=5, sticky="W", padx=(0, 10))
        Label(form, text="Width", bg='#000000', fg='#FFFFFF', font=("Montserrat", 10)).grid(row=1, column=5, sticky="W", padx=(0, 10))
        Label(form, text="Number of Trees", bg='#000000', fg='#FFFFFF', font=("Montserrat", 10)).grid(row=2, column=5, sticky="W", padx=(0, 10))

        Label(form, text="Slow Drawing", bg='#000000', fg='#FFFFFF', font=("Montserrat", 10)).grid(row=0, column=7,
                                                                                                      sticky="W",
                                                                                                      padx=(10, 10))

        def activateCheck():
            if self.treeconfig.slow_drawing == True:  # whenever checked
                # self.e7.config(state=NORMAL)
                self.treeconfig.slow_drawing = False
                # self.e7.deselect()
            elif self.treeconfig.slow_drawing == False:  # whenever unchecked
                # self.e7.config(state=ACTIVE)
                self.treeconfig.slow_drawing = True
                # self.e7.select()


        self.e1 = Entry(form, bg='#000000', fg='#FFFFFF', insertbackground='#FFFFFF', justify='center', width=7)
        self.e2 = Entry(form, bg='#000000', fg='#FFFFFF', insertbackground='#FFFFFF', justify='center', width=7)
        self.e3 = Entry(form, bg='#000000', fg='#FFFFFF', insertbackground='#FFFFFF', justify='center', width=7)
        self.e4 = Entry(form, bg='#000000', fg='#FFFFFF', insertbackground='#FFFFFF', justify='center', width=7)
        self.e5 = Entry(form, bg='#000000', fg='#FFFFFF', insertbackground='#FFFFFF', justify='center', width=7)
        self.e6 = Entry(form, bg='#000000', fg='#FFFFFF', insertbackground='#FFFFFF', justify='center', width=7)

        self.e7 = Checkbutton(form, state='normal', bg='#000000', fg='#FFFFFF', justify='center', variable=self.treeconfig.slow_drawing, command=activateCheck, onvalue=True, offvalue=False)

        self.e1.grid(row=0, column=3)
        self.e2.grid(row=1, column=3)
        self.e3.grid(row=2, column=3)
        self.e4.grid(row=0, column=6)
        self.e5.grid(row=1, column=6)
        self.e6.grid(row=2, column=6)

        self.e7.grid(row=0, column=8)

        self.i_angle_module = Image.open("angle_module.png")
        self.i_angle_module = self.i_angle_module.resize((20, 15), Image.ANTIALIAS)
        self.i_angle_module_image = ImageTk.PhotoImage(self.i_angle_module)

        self.i_levels = Image.open("levels.png")
        self.i_levels = self.i_levels.resize((20, 20), Image.ANTIALIAS)
        self.i_levels_image = ImageTk.PhotoImage(self.i_levels)

        self.i_start_height = Image.open("start_height.png")
        self.i_start_height = self.i_start_height.resize((15, 20), Image.ANTIALIAS)
        self.i_start_height_image = ImageTk.PhotoImage(self.i_start_height)

        self.i_dice = Image.open("dice.png")
        self.i_dice = self.i_dice.resize((21, 20), Image.ANTIALIAS)
        self.i_dice_image = ImageTk.PhotoImage(self.i_dice)

        self.i_trees = Image.open("trees.png")
        self.i_trees = self.i_trees.resize((21,20), Image.ANTIALIAS)
        self.i_trees_image = ImageTk.PhotoImage(self.i_trees)

        self.i_width = Image.open("width.png")
        self.i_width = self.i_width.resize((25, 12), Image.ANTIALIAS)
        self.i_width_image = ImageTk.PhotoImage(self.i_width)

        Label(form, image=self.i_angle_module_image, bg="#000000").grid(row=0, column=1, padx=5)
        Label(form, image=self.i_levels_image, bg="#000000").grid(row=1, column=1, padx=5)
        Label(form, image=self.i_start_height_image, bg="#000000").grid(row=2, column=1, padx=5)
        Label(form, image=self.i_dice_image, bg="#000000").grid(row=0, column=4, padx=5)
        Label(form, image=self.i_width_image, bg="#000000").grid(row=1, column=4, padx=5)
        Label(form, image=self.i_trees_image, bg="#000000").grid(row=2, column=4, padx=5)



        start = Button(label, bg='#000000', bd=0, text="GENERATE", fg='#FFFFFF', font='40')
        start.place(relx=0.375, rely=00, relwidth=0.25, relheigh=1)

        start.bind("<Button-1>", self.generate_tree)

        self.w.pack()

    def generate_tree(self, event):
        self.w.delete("all")
        self.treeconfig.angle_module = int(self.e1.get() if self.e1.get() != "" else self.treeconfig.angle_module)
        self.treeconfig.levels = int(self.e2.get() if self.e2.get() != "" else self.treeconfig.levels)
        self.treeconfig.d = int(self.e3.get()) * -1 if self.e3.get() != "" else self.treeconfig.d
        self.treeconfig.random_range = int(self.e4.get() if self.e4.get() != "" else self.treeconfig.random_range)
        self.treeconfig.width = int(self.e5.get()) * 0.01 if self.e5.get() != "" else self.treeconfig.width
        self.treeconfig.tree_number = int(self.e6.get() if self.e6.get() != "" else self.treeconfig.tree_number)
        # self.treeconfig.slow_drawing = bool(self.e7.get() if self.e6.get() != "" else self.treeconfig.tree_number)

    #     self.loading_gif(0)
        self.tree_cache = self.treeconfig.tree_cache
        fractree = Fractree(self.w, self.treeconfig)
        fractree.start(self.treeconfig.tree_number)

       # Progressbar(mode=“indeterminate”)




    #     self.loading_gif(1)
    #
    # def loading_gif(self, bool):
    #     loading_gif_frame = Label(root, bg='#000000')
    #     if bool == 0:
    #         loading_gif_frame.place(relx=0.47, rely=0.5, width=100, heigh=100)
    #         # PhotoImage(loading_gif_frame, 'loading.gif')
    #     if bool == 1:
    #         loading_gif_frame.place_configure()
    #         loading_gif_frame.place_forget()
    #         loading_gif_frame.destroy()



if __name__ == "__main__":
    root = Tk()
    root.title("Fractree")
    UI(root)
    root.mainloop()
