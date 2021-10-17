import numpy as np
import pytest

from sdia_python.lab2.box_window import BoxWindow


def test_raise_type_error_when_something_is_called():
    with pytest.raises(TypeError):
        # call_something_that_raises_TypeError()
        raise TypeError()


@pytest.mark.parametrize(
    "bounds, expected",
    [
        ([[2.5, 2.5]], "BoxWindow: [2.5, 2.5]"),
        ([[0, 5], [0, 5]], "BoxWindow: [0, 5] x [0, 5]"),
        (
            [[0, 5], [-1.45, 3.14], [-10, 10]],
            "BoxWindow: [0.0, 5.0] x [-1.45, 3.14] x [-10.0, 10.0]",
        ),
    ],
)
def test_box_string_representation(bounds, expected):
    assert str(BoxWindow(bounds)) == expected



@pytest.mark.parametrize(
    "bounds, expected",
    [
        ([[2, 3]], 1),
        ([[0, 5], [0, 5]], 2),
        ([[0, 1], [1, 3], [0, 3]], 3),
    ],
)
def test_dimension(bounds, expected):
    assert BoxWindow(bounds).dimension() == expected



@pytest.mark.parametrize(
    "bounds, expected",
    [
        ([[2, 3]], 1),
        ([[0, 5], [0, 5]], 25),
        ([[0, 1], [1, 3], [0, 3]], 6),
    ],
)
def test_volume(bounds, expected):
    assert BoxWindow(bounds).volume() == expected



@pytest.fixture
def example_box_window():
    bounds = [[-5, 5], [-5, 5]]
    return BoxWindow(bounds)


@pytest.mark.parametrize(
    "points, expected", [([[0, 0]], np.array([True])), ([np.array([-1, 5]),np.array([1, 2])], np.array([True, True])), ( [np.array([5, 6]),np.array([1, 2]),np.array([5,6])], np.array([False,True,False])),],
)
def test_indicator_function(example_box_window, points, expected):
    box = example_box_window
    assert ((box.indicator_function(points)) == expected).prod()==1


@pytest.mark.parametrize(
    "box, expected",
    [
        (BoxWindow([[0, 1]]), np.array([0.5])),
        (BoxWindow([[1, 2], [0, 2]]), np.array([1.5, 1])),
        (BoxWindow([[0, -4], [4, 5], [1, 3]]), np.array([-2, 4.5, 2])),
        (BoxWindow([[1, 2], [0, 2], [-4, 4], [1, 2]]), np.array([1.5, 1, 0, 1.5])),
    ],
)
def test_center(box, expected):
    assert (box.center() == expected).prod()==1


# ================================
# ==== WRITE YOUR TESTS BELOW ====
# ================================
