"""安全类评测指标。"""
from dataclasses import dataclass


@dataclass
class SafetyResult:
    collision: bool
    min_distance: float
    min_ttc: float


def check_collision(ego_traj, obstacles, threshold=0.5):
    """检测自车轨迹是否与障碍物发生碰撞。"""
    for p in ego_traj:
        for o in obstacles:
            if (p[0] - o[0]) ** 2 + (p[1] - o[1]) ** 2 < threshold ** 2:
                return True
    return False


def compute_ttc(ego_speed, lead_speed, gap):
    """计算碰撞时间 TTC = 间距 / 速度差。"""
    return gap / (ego_speed - lead_speed)
