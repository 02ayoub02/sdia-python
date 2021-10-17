import numpy as np
from math import gamma

class BallWindow:
    """class BallWindow contains balls defined by centers and radius"""
    def __init__(self, center, R):
        """initialization

        Args:
            center (array): the center
            R (float): radius of the ball
        """
        try:
            assert R >= 0
        except:
            print("Please submit a positive radius")

        try:
            # This will detect problems with center
            assert len(center) > 0
        except:
            print("Please submit a valid center")
        self.center = np.array(center, dtype = np.float32)
        self.R = R

    def __str__(self):
        """ print the ball

        Returns:
            str: BallWindow: center=..., radius=...
        """

        float_formatter = "{:.2f}".format
        np.set_printoptions(formatter={"float_kind": float_formatter})
        return (
            "BallWindow: "
            + "center="
            + str(self.center)
            + ", radius="
            + str("%.2f" % round(self.R, 2))
        )

    def indicator(self, point):
        r"""True if the point in the ball

        Args:
            point (list): point
        Returns:
            bool: True if the point in the ball
        """
        try:
            assert self.dimension() == len(point)
        except:
            print("dimension error")
        return np.sum((point - self.center) ** 2) <= self.R ** 2

        # s = 0
        # for i in range(self.dimension):
        #    s += (point[i] - self.center[i]) ** 2
        # if s <= self.radius ** 2:
        #    return True
        # return False

    def dimension(self):
        """the dimension of the ball

        Returns:
            int: dimension
        """
        return len(self.center)

    def volume(self):
        """The volume of the ball

        Returns:
            float: volume of the ball
        """
        return (
            (np.pi ** (self.dimension() / 2))
            * (self.R ** self.dimension())
            / (gamma(self.dimension() / 2 + 1))
        )

class UnitBallWindow(BallWindow):
    def __init__(self, center):

        super().__init__(center, R=1)
