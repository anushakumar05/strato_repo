from mathlib.physics import orbital_velocity

def test_orbital_velocity_positive():
    mu = 3.986e14
    r = 6.371e6
    assert orbital_velocity(mu, r) > 0
