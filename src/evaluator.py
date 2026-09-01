"""评测主流程。"""
from metrics.safety import check_collision


def evaluate(ego_traj, obstacles):
    return {"collision": check_collision(ego_traj, obstacles)}
