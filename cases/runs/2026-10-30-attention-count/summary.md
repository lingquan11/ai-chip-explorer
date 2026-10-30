# 2026-10-30 注意力两层计数表复测

> **同一 AI 三角色自评。** 模拟用户、被测助手和评价者是同一个 Cursor cloud agent（Composer 2.5）。存在自评偏差。这不是独立盲测，不是真实用户反馈，也不是在 Codex 中加载 Skill。

## 改动意图

修复 2026-10-29 深度模拟优先问题 3：`scenario-03` 临时规则里的「分数数组 0 次」易被听成零搬运。在 `references/experiences.md` 增加带 Query、Key 读取的完整计数表，不改 `SKILL.md` 主流程。

## 测试条件

- 日期：2026-10-30（Asia/Shanghai）。
- 模型：Cursor cloud agent，系统标识 **Composer 2.5**（`originalModelName` 来自本 run 的 cloud run-info）。无更细构建号，不编造版本号。
- Skill 文本：基于 `origin/main` 提交 `defe375cf62dfea9b6f02bfa2c84f5d1c2cbfbcc`（含 2026-10-30 拒绝计算草稿），再加本次 `experiences.md` 注意力两层计数段。
- 是否在 Codex 中加载 Skill：否。助手按 `SKILL.md` 与更新后的 `references/experiences.md` 角色扮演。
- 联网：本批复测未打开新网页；文献仍引用 2026-10-29 `scenario-03` 已记录的三篇摘要级来源，未重检。

## 复测场次

| 文件 | 场景 | 轮次 | 整体 |
|---|---|---|---|
| [scenario-03-rerun.md](scenario-03-rerun.md) | 已有注意力分数 idea，对照新计数表 | 9 | partial |

## 相对基线的可见变化

- 助手在第 4 轮起引用 `experiences.md` 两层表，而不是现场临时写「4 和 0」却不给跟做表。
- 模拟用户在第 6 轮质疑「0 次」后，第 7 轮用第二层合计 12 与 8 回应，未把 0 说成整体零搬运。
- 第 9 轮用户只认领 11、17；12、8、4、0 均标为按材料核对过的演示，与 2026-10-29 第 11 轮诉求一致。

## 仍未验证

- Codex 自动加载后是否会读到新段落
- 真实学生能否在 15 分钟内跟完两层表
- 角色分离重测、全文文献对照
- `python -m unittest discover -s evaluation -p "test_*.py" -v` 在本维护环境通过（3 项），只验证汇总工具

## 本批未做的事

未改 `SKILL.md` 主流程。未把模拟写成真实用户效果或稳定性证明。
