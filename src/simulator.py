"""仿真器接口（已抽象，便于从行车规控迁移到机器人运动规划）。"""


class Simulator:
    """通用运动规划仿真接口。

    行车规控与移动机器人对评测框架的需求是同构的：
    都是「给定轨迹 -> 逐帧状态 -> 指标打分」。
    因此这里只依赖轨迹数据，不绑定具体载体。
    """
    def __init__(self, scenario):
        self.scenario = scenario

    def run(self, plan):
        """输入规控轨迹，输出自车与障碍物的逐帧状态。"""
        raise NotImplementedError


class Trajectory:
    """载体无关的轨迹抽象，车与机器人通用。"""
    def __init__(self, points):
        self.points = points
