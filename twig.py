import random
import math

# angle_module = myconfig.angle_module
# angle_before = myconfig.angle_before
# old_x = myconfig.old_x
# old_y = myconfig.old_y
# levels = myconfig.levels
# d = myconfig.d
# random_range = myconfig.random_range
# start_twig_w = myconfig.start_twig_w

# parameters = myconfig.initialize()
#
# angle_module = parameters[0]
# angle_before = parameters[1]
# old_x = parameters[2]
# old_y = parameters[3]
# levels = parameters[4]
# d = parameters[5]
# random_range = parameters[6]
# start_twig_w = parameters[7]

# angle_module = 15
# angle_before = 30
# old_x = 600
# old_y = 600
# levels = 35
# d = 150
# random_range = 2
# start_twig_w = levels / 3.25


class Twig:

    def __init__(self, angle_before, old_x, old_y, level, d, start_twig_w, treeconfig):
        self.angle_before = angle_before
        self.old_x = old_x
        self.old_y = old_y
        self.level = level
        random_range = treeconfig.random_range
        angle_module = treeconfig.angle_module


        self.d = d

        d = distance_after_step(d, level)
        distance_after_step(d, level)
        random_value = angle_random_modifier(random_range)
        self.angle_after = angle_randomizer(angle_before, angle_module, random_value, level)
        self.new_x = new_xy(d, self.angle_after, old_x, old_y, level)[0]
        self.new_y = new_xy(d, self.angle_after, old_x, old_y, level)[1]
        self.twig_width = twig_width(start_twig_w, level)


def distance_after_step(d, level):
    d = d * 1 / level
    return d


def angle_random_modifier(random_range):
    # random_value = random.randint(random_range * -1, random_range)
    # random_value = random.randint(0, random_range)
    random_value = random.randint(random_range * -1, random_range * 1)
    return random_value


def angle_randomizer(angle_before, angle_module, random_value, level):
    if level == 1:
        angle_after = 90
        return angle_after
    else:
        angle_after = angle_before + (angle_module * random_value)
        return angle_after


def new_xy(d, angle_after, old_x, old_y, level):
    if level == 1:
        new_x = old_x
        new_y = old_y + d
        return new_x, new_y

    else:
        nx = math.cos(math.radians(angle_after)) * d
        ny = math.sin(math.radians(angle_after)) * d
        new_x = nx + old_x
        new_y = ny + old_y
        return new_x, new_y


def test_radians(angle_after):
    angle_radians = math.radians(angle_after)
    return angle_radians


def twig_width(start_twig_w, level):
    twig_width = start_twig_w - level
    if twig_width < 1:
        twig_width = 1
        return twig_width
    else:
        return twig_width