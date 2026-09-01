# 概念对照：工作术语 → Git 概念

| 工作中听到的话 | 对应的 Git 操作 | 本质是什么 |
| --- | --- | --- |
| 「从 develop 拉个分支改」 | `git checkout -b feature/xxx` | 复制一条独立的开发线 |
| 「把代码合进去 / 提 MR」 | `git merge` / Pull Request | 把一条线的改动并入另一条 |
| 「打个 tag 发版」 | `git tag -a v1.2.0` | 给某个提交贴一个不可变的版本标签 |
| 「线上 bug hotfix」 | 从 tag 切 `hotfix/*` 分支修复 | 在发布点上直接开最短修复线 |
| 「把修复反合回 develop」 | `git cherry-pick <hash>` | 把单个提交复制到另一条分支 |
| 「版本冻结 / 只收 bug」 | `release/*` 分支策略 | 发布前只进修复、不进新功能 |

## 四个核心对象的关系

- **commit**：一次改动快照，有唯一 hash。
- **branch**：指向某个 commit 的可移动指针（develop、feature...）。
- **tag**：指向某个 commit 的**不可移动**指针（v1.0.0）。
- **HEAD**：你当前所在的指针。

## 为什么要反合（backport）

一条 bug 在已发布版本（main）上被发现并修复后，同一个 bug 往往也存在于
还在开发的 develop 分支里。如果不把修复"反向"同步过去，下个版本又会
带上这个 bug。这个同步动作就是反合，通常用 cherry-pick 完成。
