# 维护日志

按日期记录本仓库的维护性改动。模拟测试均为同一 AI 自评时会在条目中写明，不写成真实用户效果。

## 2026-10-31：补测（1/2 第二次 + 无 Skill 对照 + knowledge-pack）

**改了什么**

- `skills/ai-chip-explorer/SKILL.md`：探索起点增加时间紧/术语/未联网就业/不因课程推验证。
- `skills/ai-chip-explorer/references/knowledge-pack.md`：无资料切换行业时不映射芯片术语、不先抛空分类。
- 新增 [cases/runs/2026-10-31-自主评估-补测/](cases/runs/2026-10-31-自主评估-补测/summary.md)（7 场 + 2 场改后复测）；更新 [cases/README.md](cases/README.md)、[STATUS.md](STATUS.md)。

**为何**

- 补 [2026-10-31-自主评估](cases/runs/2026-10-31-自主评估/summary.md) 待办：场景 1/2 第 2 次；1/2/6a 无 Skill 分离对照。
- 无 Skill 对照暴露：场景 1 量规 4「行业常态」、6a 量规 3 GEMM 误桥接。

**测试 / 限制**

- 基线 `origin/main` SHA：`aac9503`；Composer 2.5；未 Codex 加载。
- `python3 -m unittest discover -s evaluation -p "test_*.py" -v`：3 OK。
- 改后复测仍 **partial**，无 pass；模拟不代表真实用户。

**PR / commit**

- （本维护 PR 合入后在此补 merge SHA）

---

## 2026-10-31：Skill 检索默认 ≤3 与场景 4 无提示复测

**改了什么**

- `skills/ai-chip-explorer/SKILL.md`：「科研与证据」**首次检索默认 ≤3 条**；用户要求检索时**同/下轮**给模板与条目（反空转）。
- [evaluation/retrieval-record-template.md](evaluation/retrieval-record-template.md)：一句默认 ≤3 来源行（指向 SKILL）。
- 新增 [cases/runs/2026-10-31-自主评估/](cases/runs/2026-10-31-自主评估/summary.md)（11 场）；更新 [cases/README.md](cases/README.md)、[STATUS.md](STATUS.md)、[README.md](README.md) 一条亮点。

**为何**

- 上一批结论：场景 4「最多 3 篇」来自**模拟用户提示**，非 Skill 自克制；无提示时曾 **9 篇**并列（[角色分离](cases/runs/2026-10-30-角色分离/scenario-04-existing-idea-sep.md)）。

**测试 / 限制**

- 基线 `origin/main` SHA：`d3da3f7e4df51787124de3bb39c90eea62b3128f`；**Composer 2.5**；未 Codex 加载。
- **4a** 角色分离（用户/助手子代理）；用户**未**口头上限；助手 **≤3** abs + spot-check（2402.07443 等）。
- 其余场次同一 AI 三角色自评；4b/5b 刻意无 Skill fail 对照。
- `python3 -m unittest discover -s evaluation -p "test_*.py" -v`：3 OK。

**PR / commit**

- [PR #15](https://github.com/lingquan11/ai-chip-explorer/pull/15) squash merge → `16bcbe7`（合入后 `origin/main` HEAD，以仓库为准）

---

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

---

## 2026-10-30：检索记录模板与自主评估

**改了什么**

- 新增 [evaluation/retrieval-record-template.md](evaluation/retrieval-record-template.md)（来源、查阅日期、地区、阅读范围、未能验证项；「未找到 ≠ 已证明无人做过」）。
- `skills/ai-chip-explorer/SKILL.md`：科研与证据段指向该模板；[evaluation/README.md](evaluation/README.md) 同步。
- 新增 [cases/runs/2026-10-30-自主评估/](cases/runs/2026-10-30-自主评估/summary.md)（六类场景 10 场；4/5 有 Skill vs 无 Skill 对照）；更新 [STATUS.md](STATUS.md)、[cases/README.md](cases/README.md)、[README.md](README.md) 一条亮点。

**为何**

- STATUS 待办：检索记录模板 + 联网条件下重跑已有 idea / 没有 idea / 其他行业。

**测试 / 限制**

- 基线 `origin/main` SHA：`9a829278e75772911864e36fa290c29861307247`；模型 **Composer 2.5**；未 Codex 加载；同一 AI 三角色自评。
- 实际打开：arXiv abs/搜索页（见 summary）；Scholar 429。
- 场景 1、2 各类仅 1 次（第 2 次未做，原因见 summary）。
- `python3 -m unittest discover -s evaluation -p "test_*.py" -v`：3 项 OK。

**PR / commit**

- [PR #10](https://github.com/lingquan11/ai-chip-explorer/pull/10) squash merge → `41f2ed13987d57ea51e9943a8e995b5b3c19efa1`

---

## 2026-10-30：角色分离重测（场景 4 / 5 / 6）

**改了什么**

- 新增 [cases/runs/2026-10-30-角色分离/](cases/runs/2026-10-30-角色分离/summary.md) 四场完整对话 + 与自主评估批对比 summary。
- 更新 [cases/README.md](cases/README.md)、[STATUS.md](STATUS.md)。

**为何**

- STATUS 待办：检索相关场景在分开上下文中重测。

**测试 / 限制**

- 基线 SHA `f09fdb3eeba1b7a88ee16b8329662779d145e6c3`；子代理 inherit（Composer 2.5）。
- **未**完全分离：场景 4（5–8 轮）、5（4–7 轮）同代理代写；6b 单会话生成 8 轮。
- 四场 **partial**；无 Skill 代码改动。unittest 3 OK。

**PR / commit**

- [PR #12](https://github.com/lingquan11/ai-chip-explorer/pull/12) squash merge → `ae627f7eda3cd0e582ff25b494d4e475338fa1a6`（合入后 main 含该批记录；见仓库 history）

---

## 2026-10-30：角色分离补测（严格化）

**改了什么**

- 新增 [cases/runs/2026-10-30-角色分离-补测/](cases/runs/2026-10-30-角色分离-补测/summary.md)（场景 4、5、6b 各 10 轮；全程双代理；6b 非单会话）。
- 更新 [cases/README.md](cases/README.md)、[STATUS.md](STATUS.md)。

**为何**

- 上一批 `2026-10-30-角色分离` 未满足 brief：4/5 后半程代写、6b 单会话生成。

**测试 / 限制**

- 基线 `origin/main` SHA：`ae627f7eda3cd0e582ff25b494d4e475338fa1a6`；Composer 2.5 / inherit 子代理。
- arXiv abs 维护者 spot-check；评价者读摘要体 transcript。
- 三场 **partial**；**无** Skill 改动。`python3 -m unittest discover -s evaluation -p "test_*.py" -v`：3 OK。

**PR / commit**

- [PR #13](https://github.com/lingquan11/ai-chip-explorer/pull/13) squash merge → `5381127d895421ef8b6d9dc58407764adb1707bb`
