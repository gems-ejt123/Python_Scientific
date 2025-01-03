#import g constant of gravity

def vert_motion(v0, t, g=9.81):
    """A function giving the RHS of the vertical motion of a ball
       thrown up in the air.

    Parameters
    ----------
    v0 : float
        initial velocity of the ball
    t : float
        time. Should be bewtween 0 and 2*v0/g

    Returns
    -------
    float
        The 'y' position of the ball at time 't' with initial velocity 'v0'
    """

    
    return print(f'At time {t:g} and intial velocity {v0:.2f}, the height of the ball is {v0*t - (1/2)*g*t**2:.2f} meters')