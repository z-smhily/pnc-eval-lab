"""效率指标。"""


def average_speed(trajectory, dt=0.1):
    if len(trajectory) < 2:
        return 0.0
    total = sum(trajectory[i][1] * dt for i in range(1, len(trajectory)))
    return total / ((len(trajectory) - 1) * dt)
