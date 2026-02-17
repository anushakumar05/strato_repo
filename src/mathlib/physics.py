import math

DUMMY_CONSTANT = 42

def orbital_velocity(mu: float, r: float) -> float:
    """
    Compute orbital velocity.
    mu = standard gravitational parameter
    r = orbital radius
    """
    return (mu / r) ** 0.5
