"""舒适性指标。"""


def compute_jerk_rms(trajectory):
    """计算 jerk 的均方根，反映乘坐平顺性。"""
    if len(trajectory) < 3:
        return 0.0
    jerks = []
    for i in range(2, len(trajectory)):
        a1 = trajectory[i - 1][1] - trajectory[i - 2][1]
        a2 = trajectory[i][1] - trajectory[i - 1][1]
        jerks.append((a2 - a1) ** 2)
    return (sum(jerks) / len(jerks)) ** 0.5
