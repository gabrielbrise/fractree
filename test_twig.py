import twig
import pytest


def test_distance_after_step():
    assert twig.distance_after_step(300, 15) == 20


@pytest.mark.parametrize("angle_before, angle_module, random_value, level, expected", [
        (60, 30, 0, 2, 60),
        (60, 30, 1, 2, 90),
        # ("6*9", 42),
    ])
def test_angle_randomizer(angle_before, angle_module, random_value, level, expected):
    assert twig.angle_randomizer(angle_before, angle_module, random_value, level) == expected



@pytest.mark.parametrize("radians, expected", [
        (-30, -0.5235987755982988),
        (57.3248407643, 1.0005072145184977), # angulo de 57,32 graus corresponde a 1 radiano
    ])
def test_angle_radians(radians, expected):
    assert twig.test_radians(radians) == expected

@pytest.mark.parametrize("d, angle_after, old_x, old_y, level, expected", [
        (2, 30, 2, 1, 2, (3.7320508075688776, 2.0)),
        (3, -60, 4, 2, 2, (5.5, -0.598076211353316)),
        (3, 60, 4, 2, 2, (5.5, 4.598076211353316)),
        (3, 150, 4, 2, 2, (1.401923788646684, 3.5)),
        (3, -30, 4, 2, 2, (6.598076211353316, 0.5000000000000002)),
        (3, -30, 4, 2, 1, (4, 5)),
        # (57.3248407643, 1.0005072145184977), # angulo de 57,32 graus corresponde a 1 radiano
    ])
def test_new_xy(d, angle_after, old_x, old_y, level, expected):
    assert twig.new_xy(d, angle_after, old_x, old_y, level) == expected


