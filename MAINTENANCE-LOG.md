# 维护日志

按日期记录本仓库的维护性改动。模拟测试均为同一 AI 自评时会在条目中写明，不写成真实用户效果。

## 2026-10-29：深度模拟与首页亮点

**改了什么**

- 新增 `cases/runs/2026-10-29-深度模拟/`：九份多轮模拟对话（零基础×2、有基础×2、已有 idea、没有 idea×2、其他行业×2）及 [summary.md](cases/runs/2026-10-29-深度模拟/summary.md)。
- 更新 [STATUS.md](STATUS.md) 追加「2026-10-29 深度模拟」节；[cases/README.md](cases/README.md) 增加该批索引。
- 首页 [README.md](README.md)「对话会是什么样？」改为按痛点组织，亮点来自 cases 中可核查片段（经多轮 PR 收敛表述）。

**为何**

- 浅层 `cases/test-*.md` 轮次较短，需要更长模拟暴露检索、计数规则、拒绝做题等缺口。
- 让访客从 README 直接跳到有证据的对话，而不是只看抽象能力描述。

**测试 / 限制**

- Skill 基线提交 `28302bd2b1aa6a22dab7311ef237eb20c29c22ee`；Cursor cloud agent（Grok 4.7），未在 Codex 加载 Skill；同一 AI 三角色自评。
- 九次整体 `partial`；仅两场打开外部页（墨芯招聘、三篇 arXiv 摘要级）。
- `python -m unittest discover -s evaluation -p "test_*.py" -v`：汇总工具 3 项通过（维护环境用 `python3` 执行）。

**PR / commit**

- [PR #1](https://github.com/lingquan11/ai-chip-explorer/pull/1) → `4ae1b0c9c1c840b705caec5f0937a5e1dcef8258`（深度模拟记录）
- [PR #2](https://github.com/lingquan11/ai-chip-explorer/pull/2) → `68c2f6becf351933d4854e91cd400a861b331db4`；[PR #4](https://github.com/lingquan11/ai-chip-explorer/pull/4) → `a4ee624e215c3ad19b837e5c35f1f214e2365e30`；[PR #5](https://github.com/lingquan11/ai-chip-explorer/pull/5) → `4fa8a4576c37c8c1e9ac25667544be540181f54d`（README 亮点，与 #3 等同主题迭代）

---

## 2026-10-30：拒绝做题 / 无聊时的替代体验

**改了什么**

- `skills/ai-chip-explorer/references/experiences.md`：新增「当用户拒绝计算、觉得无聊或时间不够」及替代体验 E（岗位职责对照）、F（两段职责比较）；墨芯招聘页来源与 2026-10-30 查阅说明。
- `skills/ai-chip-explorer/SKILL.md`：「体验与偏好」增加一句，拒绝/无聊/时间不够时停止同类型题并指向上述草稿。
- 新增 `cases/runs/2026-10-30-refuse-calc/` 两则摘要复盘；更新 [STATUS.md](STATUS.md)、[cases/README.md](cases/README.md)。

**为何**

- 2026-10-29 深度模拟优先问题 1：`scenario-01-rerun` 拒绝纸笔后无替代，「可执行与反馈」未通过。

**测试 / 限制**

- 同一 AI 自评两则场景（拒绝计算、觉得无聊），整体 `partial`；未 Codex 加载、未角色分离。
- 注意力「0 次」计数表、检索记录模板仍待办（见下一节）。

**PR / commit**

- [PR #7](https://github.com/lingquan11/ai-chip-explorer/pull/7) squash merge → `defe375cf62dfea9b6f02bfa2c84f5d1c2cbfbcc`

---

## 2026-10-30：注意力两层读写计数表

**改了什么**

- `skills/ai-chip-explorer/references/experiences.md`：新增可选段「注意力分数——两层读写计数」（第一层分数数组 4/0，第二层含 Query/Key 元素读取合计 12/8；强调「0 次」≠ 零搬运）。
- 新增 `cases/runs/2026-10-30-attention-count/`（`scenario-03-rerun.md` + `summary.md`）；更新 [STATUS.md](STATUS.md)、[cases/README.md](cases/README.md)、本维护日志。
- 未改 `SKILL.md` 主流程。

**为何**

- 2026-10-29 `scenario-03` 第 7–8、11 轮：临时「分数数组 0 次」易被听成整体零搬运；材料库缺少可跟做表。

**测试 / 限制**

- 同一 AI（Composer 2.5）自评 1 场、9 轮，整体 `partial`；未新检索文献；用户独立重数第二层未在本场完成。
- `python3 -m unittest discover -s evaluation -p "test_*.py" -v`：3 项 OK。

**PR / commit**

- [PR #8](https://github.com/lingquan11/ai-chip-explorer/pull/8) squash merge → `b03a5bba66f552fbdeeeb38e782987a48e80db2e`
