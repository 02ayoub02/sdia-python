from sdia_python.lab2.utils import get_random_number_generator
import numpy as np


class BoxWindow:
    """class BoxWindow contains boxes  defined by intervals"""

    def __init__(self, bounds):
        """initialization

        Args:
            bounds (array): return BoxWindow of the intervals of array
        """
        # Change the array to array for more computationally efficient operations

        try:
            assert False not in (bounds[:, 1] > bounds[:, 0])
        except:
            print(
                "Please choose bounds such that it contains intervals of the form [a,b] with b > a"
            )
        self.bounds = np.array(bounds)

    def __str__(self):
        r"""BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            str: return BoxWindow: intervals
        """
        dd = "BoxWindow: "
        for i in range(len(self.bounds)):
            dd += "[" + str(self.bounds[i][0]) + ", " + str(self.bounds[i][1]) + "]"
            if i < len(self.bounds) - 1:
                dd += " x "
        return dd

    def __len__(self):
        """Takes an instance of BoxWindow class and returns number of points

        Returns:
            int: number of points
        """
        return 2 * len(self.bounds)

    def __contains__(self, point):
        """returns true if point contains in super box

        Args:
            point (array): a array containing the point's coordinates

        Returns:
            bool: returns true if point contains in the box
        """
        return True not in np.concatenate(
            (point < self.bounds[:, 0], point > self.bounds[:, 1]), axis=0
        )

    def dimension(self):
        """return the dimension of the box

        Returns:
            int: number of the intervals
        """
        return len(self.bounds)

    def volume(self):
        """calcul volume of the box

        Returns:
            float: the volume of the box
        """

        return np.prod(self.bounds[:, 1] - self.bounds[:, 0])

    def indicator_function(self, points):
        """ array of true if the each point in points in the Box

        Args:
            args (array): array of bool
        """
        l = []
        for x in points:
            l.append(x in self)
        return l

    def BoxBox(self, box):
        """verify if box in box (same dimension)

        Args:
            box (BoxWindow): box

        Returns:
            bool: verify if box in box
        """

        for i in range(len(self.bounds)):
            if box[i][0] < self.bounds[i][0] or box[i][1] > self.bounds[i][1]:
                return False
        return True

    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.
        """
        points = []
        rng = get_random_number_generator(rng)
        for i in range(n):
            point = []
            for j in range(len(self.bounds)):
                point.append(
                    (
                        (self.bounds[j][1] - self.bounds[j][0]) * rng.random()
                        + self.bounds[j][0]
                    )[0]
                )
            points.append(point)
        return points

    def center(self):
        """ return a the center of the box as array

        Returns:
            [array]: [center of box]
        """

        return np.mean(self.bounds, axis=1)


class UnitBoxWindow(BoxWindow):
    def __init__(self, dimension, center=None):
        """ initialization of a unit box window
                from a list of centers

        Args:
            dimension (int): dimension of the box
            center (array, optional): the center of the box. Defaults to None, and if that is the case we initialize centers as zeros.
        """
        if center == None:
            center = np.zeros((dimension,))
        else:
            try:
                assert len(center) == dimension
            except:
                print("center of length different than dimension")

        bounds = np.concatenate((center - 0.5, center + 0.5), axis=1)
        # bounds = [[center[i] - 0.5, center[i] + 0.5] for i in range(dimension)]
        super().__init__(bounds)
