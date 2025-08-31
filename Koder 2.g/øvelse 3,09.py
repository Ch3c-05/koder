import math

def rektangel_volume(bredde, længde):
    return længde * bredde


def kasse_volume(bredde, længde, højde):
    return rektangel_volume(bredde, længde) * højde




print(rektangel_volume (5, 10,))
print(kasse_volume(5, 10, 11))
