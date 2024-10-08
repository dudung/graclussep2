import math

def create_cluster_238_circular(diameter):
    """
    Generate lists of x, y coordinates and radii for 238 particles that
    form a circular cluster configuration.
    
    This function returns three separate lists: one for the x coordinates,
    one for the y coordinates, and one for the radii of each particle.

    Parameters:
    diameter (int): Diameter for all circular particles.
    
    
    Returns:
    tuple: A tuple containing three lists:
        - xx (list of float): The x coordinates of the particles.
        - yy (list of float): The y coordinates of the particles.
        - rr (list of float): The radii of the particles.
        
    Each list contains 238 elements, corresponding to the properties
    of each particle.
    """
    npar = 238
    dq = 2 * math.pi / 10
    xx = []
    yy = []
    rr = []
    for i in range(npar):
        if i == 0:
            x = 0
            y = 0
            xx.append(x)
            yy.append(y)
        elif 1 <= i and i <= 6:
            j = i - 1
            q = j * math.pi / 3.0
            x = diameter * math.cos(q)
            y = diameter * math.sin(q)
            xx.append(x)
            yy.append(y)
        elif 7 <= i and i <= 18:
            j = i - 7
            q = j * math.pi / 6.0
            x = 2 * diameter * math.cos(q + dq)
            y = 2 * diameter * math.sin(q + dq)
            xx.append(x)
            yy.append(y)
        elif 19 <= i and i <= 36:
            j = i - 19
            q = j * math.pi / 9.0
            x = 3 * diameter * math.cos(q + 2 * dq)
            y = 3 * diameter * math.sin(q + 2 * dq)
            xx.append(x)
            yy.append(y)
        elif 37 <= i and i <= 60:
            j = i - 37
            q = j * math.pi / 12.0
            x = 4 * diameter * math.cos(q + 3 * dq)
            y = 4 * diameter * math.sin(q + 3 * dq)
            xx.append(x)
            yy.append(y)
        elif 61 <= i and i <= 90:
            j = i - 61
            q = j * math.pi / 15.0
            x = 5 * diameter * math.cos(q + 4 * dq)
            y = 5 * diameter * math.sin(q + 4 * dq)
            xx.append(x)
            yy.append(y)
        elif 91 <= i and i <= 126:
            j = i - 91
            q = j * math.pi / 18.0
            x = 6 * diameter * math.cos(q + 5 * dq)
            y = 6 * diameter * math.sin(q + 5 * dq)
            xx.append(x)
            yy.append(y)
        elif 127 <= i and i <= 168:
            j = i - 127
            q = j * math.pi / 21.0
            x = 7 * diameter * math.cos(q + 6 * dq)
            y = 7 * diameter * math.sin(q + 6 * dq)
            xx.append(x)
            yy.append(y)
        elif 169 <= i and i <= 216:
            j = i - 169
            q = j * math.pi / 24.0
            x = 8 * diameter * math.cos(q + 7 * dq)
            y = 8 * diameter * math.sin(q + 7 * dq)
            xx.append(x)
            yy.append(y)
        elif 217 <= i and i <= 238:
            j = i - 217
            q = j * math.pi / 21.0 * 2
            x = 9 * diameter * math.cos(q + 8 * dq)
            y = 9 * diameter * math.sin(q + 8 * dq)
            xx.append(x)
            yy.append(y)
        else:
            pass
        rr.append(0.5 * diameter)
    return xx, yy, rr
