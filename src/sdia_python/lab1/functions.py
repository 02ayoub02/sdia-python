def is_unique(x):
    """verify that all elemens of list are not repeated

    Args:
        x (list): list of elements

    Returns:
        bool: True if all elemens of list are not repeated

    """
    return len(x) == len(set(x))


def triangle_shape(height):
    """return a triangle of x

    Args:
        height (int): number of stages

    Returns:
        str: triangle
    """
    s = "x"
    esp = " "
    if height == 0:
        return ""
    return "\n".join(
        [
            (height - 1 - i) * esp + (2 * i + 1) * s + (height - 1 - i) * esp
            for i in range(height)
        ]
    )
