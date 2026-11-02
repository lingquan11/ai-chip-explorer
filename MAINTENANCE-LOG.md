# 维护日志

按日期记录本仓库的维护性改动。模拟测试均为同一 AI 自评时会在条目中写明，不写成真实用户效果。

## 2026-11-02：用户可见用语、两层计数与 12 场评估

**改了什么**

- `skills/ai-chip-explorer/SKILL.md`：对用户不用 A–G 编号；第二次 boring 不轮换第三种；有 idea 时两层计数同轮、区分已发表工作与待验证假设。
- `skills/ai-chip-explorer/references/experiences.md`：助手应做到增加不对用户暴露编号、第二次 boring 结束；两层计数须同轮呈现。
- 新增 [cases/runs/2026-11-02-自主评估/](cases/runs/2026-11-02-自主评估/summary.md)；更新 [cases/README.md](cases/README.md)、[STATUS.md](STATUS.md)。

**为何**

- [2026-11-01 1a](cases/runs/2026-11-01-自主评估/scenario-01-beginner-misinterest-sep.md) 等：助手对用户说「G 式」等内部编号，用户听不懂。
- [2026-10-29 深度模拟 scenario-03](cases/runs/2026-10-29-深度模拟/scenario-03.md)：分数层「0 次」易被听成零搬运。

**测试 / 限制**

- 基线 `origin/main` SHA：`e0a5202`；Composer 2.5；未 Codex 加载。
- arXiv abs：2402.07443、2406.10491、2111.12885、2505.12665 HTTP 200（摘要级）。
- `python3 -m unittest discover -s evaluation -p "test_*.py" -v`：3 OK。
- 仍无整体 pass；子代理分离 ≠ 盲测。

**PR / commit**

- （合入后补 PR 链接与 merge SHA）

---

## 2026-11-01：替代 G、检索相关性与 12 场评估

**改了什么**

- `skills/ai-chip-explorer/references/experiences.md`：新增 **替代体验 G**（用户拒手算且拒招聘/JD 时的口语化方向对照，无网页）。
- `skills/ai-chip-explorer/SKILL.md`：体验段指向 E/F/**G**；科研段 ≤3 须与用户 problem **直接相关**、禁止无关凑数、旁证须同轮说明；体验偏好强化不得从单次体验/粗计时推适合性。
- 新增 [cases/runs/2026-11-01-自主评估/](cases/runs/2026-11-01-自主评估/summary.md)（12 场 + 复测 + 3/4 无 Skill 对照）；更新 [cases/README.md](cases/README.md)、[STATUS.md](STATUS.md)。

**为何**

- [2026-10-31 3a](cases/runs/2026-10-31-自主评估/scenario-03-refuse-time.md)：拒招聘后缺低负担路径。
- [2026-10-31 4a](cases/runs/2026-10-31-自主评估/scenario-04-existing-attention-with-skill-retest.md)：第 3 条 GEMMFIP 与用户 attention  framing 过宽。

**测试 / 限制**

- 基线 `origin/main` SHA：`b857c33`；Composer 2.5；未 Codex 加载。
- arXiv abs：2402.07443、2406.10491、2111.12885、2505.12665 HTTP 200（摘要级）。
- `python3 -m unittest discover -s evaluation -p "test_*.py" -v`：3 OK。
- 仍无整体 pass；子代理分离 ≠ 盲测。

**PR / commit**

- [PR #19](https://github.com/lingquan11/ai-chip-explorer/pull/19) squash merge → **`b07366e`**

---

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

- [PR #17](https://github.com/lingquan11/ai-chip-explorer/pull/17) squash merge → **`e3d9e9b6a80d29fb679ad378dad523eabefda4b2`**

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

## 2026-11-02 矩阵乘预测对照辅助

新增 learner-aids 中一节与 SKILL 指针。只读核查 cpp-matmul-performance 的 src/day07-matrix-blocking.cpp：int 静态数组、MAX_N=256、sizes 固定、无命令行参数、CSV 写当前目录；三个 256 阶 int 矩阵按 4 字节估算为 768 KiB，须注意 C++ int 大小以实际平台为准。experiments/summarize_medians.py 固定读取 Day 5/7 历史 CSV，不读取新运行文件。

验证：python -m unittest discover -s evaluation -p "test_*.py" -v：3 tests OK；汉字计数小节 466、全文 553、指针 49。维护者脚本化模拟见 cases/runs/2026-11-02-learner-aids-matmul/summary.md，最多 partial，非安装后实测或真实用户；按小节读取仍待核验。是否保留 blocked 对照及扩展规模由零醛决定。

## 2026-11-02 I1 反例题库

新增 `skills/ai-chip-explorer/references/counterexamples.md`（文件头规则、错因标签、4 张陷阱卡 CE-01～CE-04、本地日志格式）；`experiences.md` 在「体验回顾」末尾加一行指针；`.gitignore` 追加 `personal-logs/`。未改 SKILL.md 主流程。

数字核对：CE-01、CE-02、CE-03 的正确答案与 experiences.md 对应参考答案逐项一致；陷阱答案为手算。CE-04 的 12 与 8 出自两层计数表，改成「Q 只读一次」后的 10 与 6 是按同一计数约定重数的结果，设计稿推算相同，但不在 experiences.md 中。

未验证：CE-04 的 10 与 6 待零醛复核；4 张卡的难度和迷惑性未经真实用户试跑；Codex 等平台实际加载未验证；`personal-logs/` 仅为忽略规则，未建日志文件。验证命令：`python -m unittest discover -s evaluation -p "test_*.py" -v`（结果见 PR 说明）。
