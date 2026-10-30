# 项目状态

更新：2026-10-30。维护者应根据实际运行结果更新，不应凭文件存在就写成已验证。维护改动按日期见 [MAINTENANCE-LOG.md](MAINTENANCE-LOG.md)。

## 范围

第一版目标：Codex 优先；AI 芯片方向全景、四个轻量体验、科研 idea 辅助、可替换行业资料、手动模拟评估包和中文说明。未来考虑其他 agent 与更多行业。

## 需要核实的状态

- Skill 元数据：使用 skill-creator quick_validate.py 检查通过；本地 Markdown 相对链接检查无缺失；不能据此证明对话效果。引用路径需随每次变更继续核对。
- Codex 安装、自动发现和真实对话行为：待实际测试。
- 四个轻量体验：步骤、依赖和实际耗时分别待试跑。
- 模拟测试：2026-10-29 覆盖初学者、已有 idea、无 idea、其他行业四个场景，各 1 次、每次 6–7 轮；均由同一代理模拟用户、助手并自评，结果为部分通过。未联网、未实际安装 Skill、未独立盲测或重复运行；不应声称稳定性或真实用户效果已得到证明。详情见 `cases/README.md`。
- 评估汇总工具：`python -m unittest discover -s evaluation -p "test_*.py" -v`，3 项通过；只检验汇总工具，不代表 Skill 测试结果。
- 外部行业知识库：不同文件、网页、论文及权限条件下的实际读取能力待测试。
- 岗位和方向资料：随着时间变化，应记录查阅日期并定期复核。
- DeepSeek agent：后续适配，尚未验证。
- GitHub：主仓库已创建为公开仓库；用户决定案例和成果统一放在主仓库的 `cases/` 中。
- 许可证：尚未选择；发布或复用外部内容前需核查。

## 测试后的优先改进

- 设计实验时补充明确的模型假设、计数规则和可跟做的具体例子，确认初学者可以执行。
- 在联网条件下测试论文与岗位检索，记录来源、时间、覆盖范围和无法验证的内容。
- 使用角色、被测助手与评价者分离的方式重复测试，并保留失败案例；验证 Codex 实际加载与用户体验。

## 维护记录

每次修改请补充日期、改动、证据来源、验证命令及结果、未验证部分和后续事项。若有模拟结果，记录模型及版本、日期、环境、次数、角色、对话、评分依据和失败项。


### 2026-10-30 拒绝计算替代体验

- 日期：2026-10-30（Asia/Shanghai）。
- 改动：`skills/ai-chip-explorer/references/experiences.md` 增加「当用户拒绝计算、觉得无聊或时间不够」及替代体验 E/F；`SKILL.md`「体验与偏好」增加一句，拒绝、无聊或时间不够时停止同类型题并指向该段。新增案例目录 `cases/runs/2026-10-30-refuse-calc/`。
- 证据来源：墨芯「加入我们」页，查阅日期 2026-10-30；阅读范围为校招岗位标题、地点、职责与技能条目；未见岗位发布日期；页脚版权年显示 2025。样本只有一家公司。
- 验证：同一 AI 扮演模拟用户、被测助手和评价者，做了两则摘要级复盘（拒绝计算、觉得无聊），整体均为 partial。没有在 Codex 中加载 Skill。
- 未验证：Codex 安装与自动发现、真实学生试跑、角色分离重测。详见 [MAINTENANCE-LOG.md](MAINTENANCE-LOG.md) 2026-10-30 拒绝计算条目（[PR #7](https://github.com/lingquan11/ai-chip-explorer/pull/7) → `defe375cf62dfea9b6f02bfa2c84f5d1c2cbfbcc`）。这不是独立盲测，也不能写成真实用户效果。

### 2026-10-30 注意力两层计数表

- 日期：2026-10-30（Asia/Shanghai）。
- 改动：`references/experiences.md` 增加可选「注意力分数——两层读写计数」；新增 `cases/runs/2026-10-30-attention-count/`；[MAINTENANCE-LOG.md](MAINTENANCE-LOG.md) 追加本批说明。未改 `SKILL.md` 主流程。
- 验证：Composer 2.5 同一 AI 自评 1 场（`scenario-03-rerun`），9 轮，整体 partial。`python3 -m unittest discover -s evaluation -p "test_*.py" -v`：3 项 OK。
- 未验证：Codex 是否读到新段落、学生跟做第二层表、角色分离与全文文献。

### 2026-10-30 检索模板与自主评估

- 日期：2026-10-30（Asia/Shanghai）。
- 改动：新增 [evaluation/retrieval-record-template.md](evaluation/retrieval-record-template.md)；`SKILL.md`「科研与证据」与 [evaluation/README.md](evaluation/README.md) 引用该模板。新增 `cases/runs/2026-10-30-自主评估/`（10 场 + [summary](cases/runs/2026-10-30-自主评估/summary.md)）。
- 联网检索（维护会话，摘要级）：arXiv abs 2402.07443、2406.10491、2111.12885、2505.12665；Google Scholar 429 未用。
- 验证：`python3 -m unittest discover -s evaluation -p "test_*.py" -v` 3 项 OK。同一 AI（Composer 2.5）自评；4a/5a 有 Skill partial；4b/5b 无 Skill 对照 fail（脚本化，非盲测）。
- 未完成：场景 1、2 各类第 2 次；Codex 加载。详见 [MAINTENANCE-LOG.md](MAINTENANCE-LOG.md) 本日条目。

### 2026-10-30 角色分离重测（场景 4 / 5 / 6）

- 日期：2026-10-30（Asia/Shanghai）。
- 改动：新增 `cases/runs/2026-10-30-角色分离/`（4 场 + [summary](cases/runs/2026-10-30-角色分离/summary.md)）；**未改** Skill/references。
- 分离：子代理 inherit（Composer 2.5）；场景 4/5 **部分轮次同代理代写**（见 summary）；6b **非**逐轮双代理。
- 检索：2106.10499、2505.12665 等 abs 摘要级；场景 4 助手一轮列举 9 篇，**未全量 spot-check**。
- 验证：独立评价者子代理；四场整体 **partial**。`python3 -m unittest discover -s evaluation -p "test_*.py" -v`：3 项 OK。
- 未完成：Codex、无 Skill 分离对照。对比 [自主评估](cases/runs/2026-10-30-自主评估/summary.md) 见角色分离 summary。

### 2026-10-30 角色分离补测（严格化）

- 日期：2026-10-30（Asia/Shanghai）。
- 改动：新增 `cases/runs/2026-10-30-角色分离-补测/`（场景 4/5/6b 各 1 场、**8–12 轮**取 10 轮）；**未改** Skill/references。
- 分离：用户/助手 **全程** 独立子代理；6b **逐轮** 双代理（非单会话）。评价者独立。
- 检索：listed arXiv abs 维护者 HTTP 核实（见补测 summary）；read_scope 摘要级。
- 验证：`python3 -m unittest discover -s evaluation -p "test_*.py" -v`：3 项 OK。三场 **partial**。
- 未完成：6a 分离、Codex、无 Skill 分离对照。见 [补测 summary](cases/runs/2026-10-30-角色分离-补测/summary.md)。


## 2026-10-29 深度模拟（追加，不替换上文）

上文的四次浅层模拟仍然有效。本节只追加当天晚些时候的一批更长记录，不把它们写成已经验证的用户效果。

- 日期：2026-10-29（Asia/Shanghai）。文献与招聘页查阅时间约 20:15（CST）。
- Skill 提交：`28302bd2b1aa6a22dab7311ef237eb20c29c22ee`。
- 执行者：Cursor cloud agent，系统标识 Grok 4.7。没有更细的构建号，不编造版本号。
- 条件：没有在 Codex 中加载 Skill。同一个 AI 扮演模拟用户、被测助手和评价者。宿主有网络；只有两个文件实际打开了外部页面，其余场次未检索。
- 记录：[cases/runs/2026-10-29-深度模拟/summary.md](cases/runs/2026-10-29-深度模拟/summary.md)。

### 已完成

- 写完九份对话：零基础 2 次、学过编程和数字电路 2 次、已有 idea 1 次、没有 idea 2 次、农业机器人且无知识库 1 次、另加一份粘贴虚构笔记的行业对话。每份 9–11 轮。
- 九次整体评价都是部分通过。scenario-01-rerun 的“可执行与反馈”为未通过，已保留。
- 旧的 `cases/test-*.md` 四份文件没有改内容。`SKILL.md` 与 `references/` 没有改流程。

### 已验证

- 测试开始时 `origin/main` 的完整 SHA 是 `28302bd2b1aa6a22dab7311ef237eb20c29c22ee`。这只验证了当时的提交位置，不验证对话质量。
- 2026-10-29 20:15（CST）打开 `https://www.moffettai.com/jia-ru-wo-men/`。页面上的算子开发校招写硕士及以上，架构开发校招写硕士或博士及 Verilog / SystemVerilog；岗位条目没有看到发布日期；页脚版权年为 2025。只说明这一页在当时如此，不说明行业或该页现在仍相同。
- 同一时间用检索式 `attention accelerator dataflow memory traffic QK matrix 2024` 打开了三篇文献的摘要和引言开头：arXiv:2402.07443、arXiv:2406.10491、`https://arxiv.org/html/2404.16629`。未读全文，未复现实验。PMLR 与 ACM 版本页没有通读。

### 待办

- ~~在 `references/experiences.md` 为“拒绝计算”的用户补一个替代入口草稿~~ **2026-10-30 已完成**（[PR #7](https://github.com/lingquan11/ai-chip-explorer/pull/7)）：替代体验 E/F；见 `cases/runs/2026-10-30-refuse-calc/`。
- ~~为注意力分数补不会把“0 次”听成零搬运的计数表~~ **2026-10-30 已完成**：两层计数写入 `references/experiences.md`；同一 AI 自评见 `cases/runs/2026-10-30-attention-count/`（merge SHA 见 [MAINTENANCE-LOG.md](MAINTENANCE-LOG.md)）。
- ~~增加检索记录模板~~ **2026-10-30 已完成**（见 [retrieval-record-template.md](evaluation/retrieval-record-template.md) 与 `cases/runs/2026-10-30-自主评估/`）；**严格角色分离**重跑见 `cases/runs/2026-10-30-角色分离/`（**部分轮次仍代写**，非 Codex 盲测）。
- 过一段时间复查上述招聘页是否仍然没有发布日期。
- Codex 安装、自动发现、四道练习的学生试跑、许可证，仍未做。上文已有的待办继续有效。

### 局限

同一 AI 自评，检索式和笔记中的陷阱句都由这个代理设计。不能写成稳定性、就业判断或科研新颖性已得到验证。详情和对话轮次见案例目录中的 `summary.md`。
