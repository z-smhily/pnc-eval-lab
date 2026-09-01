"""命令行入口。"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.evaluator import evaluate


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scenario", default="urban_cutin")
    args = ap.parse_args()
    ego = [(i * 0.1, 10.0) for i in range(20)]
    obstacles = [(50.0, 10.0)]
    print(f"scenario={args.scenario}", evaluate(ego, obstacles))


if __name__ == "__main__":
    main()
