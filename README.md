# PNC Eval Lab — 行车规控仿真评测框架

一个用于练习 **Git 版本发布流程** 的仿真评测项目。业务背景：智能驾驶
行车规控（Planning & Control）算法的仿真评测。

项目本身是可运行的 Python（无第三方依赖），但真正的学习目标是仓库里的
**分支、tag、合入与反合历史**。

## 快速开始

```bash
python scripts/run_eval.py --scenario urban_cutin
```

## 目录

- `config/`   评测配置与场景集
- `metrics/`  安全 / 舒适 / 效率指标
- `src/`      仿真器接口与评测主流程
- `reports/`  评测报告输出目录

## 练习

打开 `EXERCISES.md`，从练习 0 开始。概念不清楚时看 `CONCEPTS.md`。
