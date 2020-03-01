import twig


class Fractree:

    def __init__(self, w, treeconfig):
        self.canvas = w
        self.treeconfig = treeconfig

    def twig_creator(self, angle_before, old_x, old_y, level, d):
        start_twig_w = self.treeconfig.levels * self.treeconfig.width
        new_twig = twig.Twig(angle_before, old_x, old_y, level, d, start_twig_w, self.treeconfig)
        # old_x = new_twig.old_x
        # old_y = new_twig.old_y
        new_x = new_twig.new_x
        new_y = new_twig.new_y
        angle_before = new_twig.angle_before
        angle_after = new_twig.angle_after

        if new_x == old_x and level != 1 or angle_after == angle_before or level == 2:
            new_branch_levels = self.treeconfig.levels - level
            new_branch_level = level + 1
            self.tree_generator(angle_before, old_x, old_y, new_branch_levels, new_branch_level, d)
            # w.create_line(old_x, old_y, new_x, new_y, width=new_twig.twig_width, capstyle='round')
            self.twig_colored(old_x, old_y, new_x, new_y, new_twig, level)
            return new_twig
        #
        # if level != 1:
        #     new_branch_levels = self.treeconfig.levels - level
        #     new_branch_level = level + 1
        #     self.tree_generator(angle_before, old_x, old_y, new_branch_levels, new_branch_level, d)
        #     # w.create_line(old_x, old_y, new_x, new_y, width=new_twig.twig_width, capstyle='round')
        #     self.twig_colored(old_x, old_y, new_x, new_y, new_twig, level)
        #     return new_twig

        else:

            # w.create_line(old_x, old_y, new_x, new_y, width=new_twig.twig_width, capstyle='round')
            self.twig_colored(old_x, old_y, new_x, new_y, new_twig, level)
            return new_twig

    def twig_colored(self, old_x, old_y, new_x, new_y, new_twig, level):
        if level > self.treeconfig.levels * .75 and level != self.treeconfig.levels:
            # w.create_line(old_x, old_y, new_x, new_y, width=new_twig.twig_width, capstyle='round', fill='#afafaf')
            # self.canvas.create_line(old_x, old_y, new_x, new_y, width=new_twig.twig_width, capstyle='round', fill='#858585')

            self.canvas.create_line(old_x, old_y, new_x, new_y, width=new_twig.twig_width, capstyle='round', fill='#afafaf')

        elif level == self.treeconfig.levels:
            # self.canvas.create_oval(old_x + ((old_x - new_x) / 2), old_y, new_x, new_y, outline="#e55032", fill="#e55032")
            # self.canvas.create_oval(old_x, old_y, old_x + 3, old_y + 6, outline="#858585", fill="#858585")
            return
            # w.create_line(old_x, old_y, new_x, new_y, width=new_twig.twig_width, capstyle='round', fill='#000000')
            # w.create_line(old_x, old_y, new_x, new_y, width=new_twig.twig_width, capstyle='round', fill='#FFFFFF')

        else:
            self.canvas.create_line(old_x, old_y, new_x, new_y, width=new_twig.twig_width, capstyle='round', fill='#000000')
            # w.create_line(old_x, old_y, new_x, new_y, width=new_twig.twig_width, capstyle='round', fill='#FFFFFF')

    def tree_generator(self, angle_before, old_x, old_y, levels, level, d):
        tree = []


        for i in range(levels):
            new_twig = self.twig_creator(angle_before, old_x, old_y, level, d)
            tree.append(new_twig)
            angle_before = new_twig.angle_after
            old_x = new_twig.new_x
            old_y = new_twig.new_y
            level = new_twig.level + 1
            d = new_twig.d
            print(tree)

            # self.treeconfig.tree_cache.append(NewTwig(old_x, old_y, new_twig.new_x, new_twig.new))

            if self.treeconfig.slow_drawing is True:
                self.canvas.update_idletasks()




    def start(self, tree_number):
        # w.create_rectangle(2500, 2500, 0, 675, fill="#000000", outline="#000000")
        # screen_w = 1920
        screen_w = 1536
        screen_h = 1080
        # self.treeconfig.old_y = screen_h - (screen_h / 10)
        for i in range(tree_number):
            tree_number_module = screen_w / (tree_number + 1)
            self.treeconfig.old_x = (tree_number_module * i) + tree_number_module
            self.tree_generator(self.treeconfig.angle_before, self.treeconfig.old_x, self.treeconfig.old_y, self.treeconfig.levels, 1, self.treeconfig.d)
        # self.tree_generator(self.treeconfig.angle_before, 350, 600, self.treeconfig.levels, 1, self.treeconfig.d)
        # tree_generator(angle_before, 450, old_y, levels, 1, d)
        # tree_generator(angle_before, 1050, old_y, levels, 1, d)
        # tree_generator(angle_before, 1350, old_y, levels, 1, d)

    def test(self):
        print("Ta funcionando")


# UI.start(p)



# w.pack()
# root.mainloop()
# root.tk.call('tk', 'scaling', '-displayof', '.', 5)
