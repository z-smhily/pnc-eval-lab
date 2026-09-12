"""评测主流程。"""
from metrics.safety import check_collision
from metrics.comfort import compute_jerk_rms
from metrics.efficiency import average_speed


def evaluate(ego_traj, obstacles):
    return {
        "collision": check_collision(ego_traj, obstacles),
        "jerk_rms": compute_jerk_rms(ego_traj),
        "avg_speed": average_speed(ego_traj),
    }
