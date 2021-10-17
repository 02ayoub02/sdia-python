import numpy as np
import pytest


from sdia_python.lab2.ball_window import BallWindow


# def test_raise_type_error_when_something_is_called():
#     with pytest.raises(TypeError):
#         # call_something_that_raises_TypeError()
#         pass


# ================================
# ==== WRITE YOUR TESTS BELOW ====
# ================================


@pytest.mark.parametrize(
    "center, R, expected",
    [
        ([2, 1], 2, "BallWindow: center=[2.00 1.00], radius=2.00"),
        ([0, 5, 1], 3, "BallWindow: center=[0.00 5.00 1.00], radius=3.00"),
        (
            [0, 5, -1.45, 3.14],
            np.sqrt(2),
            "BallWindow: center=[0.00 5.00 -1.45 3.14], radius=1.41"
        ),
    ],
)
def test_ball_string_representation(center, R, expected):
    assert str(BallWindow(center, R)) == expected


@pytest.fixture
def example_ball_window():
    center = [2, 1]
    R = 2.0
    return BallWindow(center, R)


@pytest.mark.parametrize(
    "points, expected",
    [
        ([0, 0], False),
        ([0, 1], True),
        ([5, 6], False),
    ],
)
def test_indicator(example_ball_window, points, expected):
    ball = example_ball_window
    assert ball.indicator(points) == expected


@pytest.mark.parametrize(
    "ball, expected",
    [
        (BallWindow([0, 1], 1), np.pi),
        (BallWindow([1, 0, 2], 3), 113.09733552923254),
        (BallWindow([0, -4, 1, 3], 3), 399.718978244119),
    ],
)
def test_volume(ball, expected):
    assert (ball.volume()) == expected
