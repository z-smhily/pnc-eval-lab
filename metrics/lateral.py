"""横向误差指标（开发中）。"""


def max_lateral_error(ego_traj, ref_traj):
    """计算相对参考线的最大横向偏差。"""
    if not ego_traj or not ref_traj:
        return 0.0
    return max(abs(a[1] - b[1]) for a, b in zip(ego_traj, ref_traj))
