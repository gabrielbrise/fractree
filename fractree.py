import twig
import tkinter as tk
from PIL import ImageTk
import random


class Fractree:

    def __init__(self, w, treeconfig):
        self.canvas = w
        self.treeconfig = treeconfig

        window = tk.Tk()
        height = window.winfo_screenheight()
        width = window.winfo_screenwidth()
        window.destroy()
        self.treeconfig.old_x = width / 2
        self.treeconfig.old_y = height * 0.85
        self.tree = []

    def twig_creator(self, angle_before, old_x, old_y, level, d):
        start_twig_w = self.treeconfig.levels * self.treeconfig.width
        new_twig = twig.Twig(angle_before, old_x, old_y,
                             level, d, start_twig_w, self.treeconfig)
        new_x = new_twig.new_x
        new_y = new_twig.new_y
        angle_before = new_twig.angle_before
        angle_after = new_twig.angle_after

        if new_x == old_x and level != 1 or angle_after == angle_before or level == 2:
            new_branch_levels = self.treeconfig.levels - level
            new_branch_level = level + 1
            self.tree_generator(angle_before, old_x, old_y,
                                new_branch_levels, new_branch_level, d)
            # w.create_line(old_x, old_y, new_x, new_y, width=new_twig.twig_width, capstyle='round')
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
            return new_twig

    def render_twig(self, tree):
        for i in tree:
            color = "#afafaf" if i.level > self.treeconfig.levels * \
                .75 and i.level != self.treeconfig.levels else "#000000"
            self.canvas.create_line(
                i.old_x, i.old_y, i.new_x, i.new_y, width=i.twig_width, capstyle='round', fill=color)

    def tree_generator(self, angle_before, old_x, old_y, levels, level, d):

        for i in range(levels):
            new_twig = self.twig_creator(angle_before, old_x, old_y, level, d)
            self.tree.append(new_twig)
            angle_before = new_twig.angle_after
            old_x = new_twig.new_x
            old_y = new_twig.new_y
            level = new_twig.level + 1
            d = new_twig.d

            if self.treeconfig.slow_drawing is True:
                self.canvas.update_idletasks()

    def start(self, tree_number):
        window = tk.Tk()
        height = window.winfo_screenheight()
        width = window.winfo_screenwidth()
        window.destroy()
        screen_w = width
        screen_h = height
        for i in range(tree_number):
            tree_number_module = screen_w / (tree_number + 1)
            self.treeconfig.old_x = (
                tree_number_module * i) + tree_number_module
            self.tree_generator(self.treeconfig.angle_before, self.treeconfig.old_x,
                                self.treeconfig.old_y, self.treeconfig.levels, 1, self.treeconfig.d)
        # self.export_to_png()
        self.render_twig(self.tree)
