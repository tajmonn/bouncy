def calculate_speed(speed, falloff):
    x = abs(speed)
    x = x**falloff
    if speed < 0:
        x = -x
    return x


def calculate_friction(speed, friction):
    x = abs(speed)
    if x < 2:
        return 0
    x -= 1
    x = x**friction
    if speed < 0:
        x = -x
    return x
