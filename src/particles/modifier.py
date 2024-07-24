import random

def set_charge(xx, yy, rr, charge=1, num=92, mode='random'):
    """
    Set charge for particles previously defined by x, y coordinates and
    radii that form a certain cluster configuration.
    
    This function returns a list of charges of particles.

    Parameters:
    num (int): Number of particles to have value other than default 0.
    mode (string): Mode how to modify the charges:
        - 'first': set num charges in the beginning of the list.
        - 'last': set num charges in the end of the list.
        - 'random': set num charges at random position in the list.
    
    Returns:
    qq (list of float): The charges of particles.
        
    The list contains elements, corresponding to the charge of each
    particle.
    """
    n = min(len(xx), len(yy), len(rr))
    qq = [0] * n
    if mode == 'first':
        qq[0:num] = [charge] * num
    elif mode == 'last':
        qq[-num:] = [charge] * num
    elif mode == 'random':
        j = 0;
        for i in range(n):
            rnd = random.random()
            if j >= num:
                break
            if rnd > 0.5:
                qq[i] = charge;
                j += 1
    else:
        pass
    return qq
