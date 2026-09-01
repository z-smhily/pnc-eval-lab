"""仿真器基础接口。"""


class Simulator:
    def __init__(self, scenario):
        self.scenario = scenario

    def run(self, plan):
        """输入规控轨迹，输出自车与障碍物的逐帧状态。"""
        raise NotImplementedError
