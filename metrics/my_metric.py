"""平均航向角误差指标（练习用）。"""


def mean_heading_error(ego_headings, ref_headings):
    """计算自车相对参考线的平均航向角误差。

    Args:
        ego_headings: 自车逐帧航向角（弧度）列表
        ref_headings: 参考线逐帧航向角（弧度）列表

    Returns:
        平均绝对航向误差（弧度）
    """
    if not ego_headings or not ref_headings:
        return 0.0
    n = min(len(ego_headings), len(ref_headings))
    errors = [abs(e - r) for e, r in zip(ego_headings[:n], ref_headings[:n])]
    return sum(errors) / n
