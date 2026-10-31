# 模拟对话案例

2026-10-29：四个场景各进行一次多轮角色扮演式试运行，记录如下。每次均由同一代理模拟用户、助手并自评，未联网、未实际安装或自动发现 Skill；有明显自评偏差，具体模型版本未独立记录。四次均为部分通过，不能据此评估跨运行稳定性。

| 场景 | 可观察到的回应 | 尚未完成 |
|---|---|---|
| [零基础探索](test-beginner.md) | 将性能兴趣转化为低负担的算子体验，并追问感受 | 未检索可核查的实际岗位来源 |
| [已有 idea](test-existing-idea.md) | 沿用户的数据搬运想法收窄问题，标明新颖性未知 | 手算模型规则和具体计数尚未完成 |
| [没有 idea](test-no-idea.md) | 基于条件给出两个候选方向，并承认可能与已有工作重叠 | 未检索论文，验证计划的计数规则尚不充分 |
| [其他行业、资料不足](test-other-domain.md) | 明确无资料与无网络，提供标明假设的探索步骤 | 行业分类与体验未经资料核查或实际试跑 |

每个案例均保留完整模拟对话、量规判断和限制。未来继续记录运行模型和条件、关键对话、结果、失败或限制，公开前检查内容与权限。

这些案例是模拟用户体验，不能单独证明真实用户效果或整体稳定性。未运行时不得编造表现、评分或用户评价。

## 2026-10-29 深度模拟

当天在上述四份浅层记录之外，另做了一批更长的角色扮演。旧的四份案例没有改写。新记录在 [runs/2026-10-29-深度模拟/](runs/2026-10-29-深度模拟/summary.md)。

条件：Skill 提交 `28302bd2b1aa6a22dab7311ef237eb20c29c22ee`；Cursor cloud agent，系统标识 Grok 4.7，无更细构建号；没有在 Codex 中加载 Skill。同一个 AI 扮演用户、助手和评价者，存在自评偏差，不是独立盲测，也不是真实用户反馈。九次整体都是部分通过。

| 场景 | 次数 | 完整对话 | 本轮可见结果 | 仍未解决 |
|---|---|---|---|---|
| 零基础，怕负担 | 2 | [第 1 次](runs/2026-10-29-深度模拟/scenario-01.md)、[第 2 次](runs/2026-10-29-深度模拟/scenario-01-rerun.md) | 第 1 次停在一个矩阵元素；第 2 次打开一家公司招聘页并写明没有发布日期 | 拒绝做题时没有替代体验，给不出方向建议 |
| 学过编程和数字电路 | 2 | [第 1 次](runs/2026-10-29-深度模拟/scenario-02.md)、[第 2 次](runs/2026-10-29-深度模拟/scenario-02-rerun.md) | 偏好不同时，第一题从比较写法换成加法 | 用户觉得加法无聊后，助手仍多要了一组输入 |
| 已有 idea | 1 | [注意力搬运](runs/2026-10-29-深度模拟/scenario-03.md) | 列出当次读过摘要的三篇文献，用户只承认自己算了两个分数 | 全文未读；临时计数规则容易被听成零搬运 |
| 没有 idea | 2 | [数据流动](runs/2026-10-29-深度模拟/scenario-04.md)、[低精度](runs/2026-10-29-深度模拟/scenario-04-rerun.md) | 两次都停在短练习，并写明那不是科研 idea | 未检索，不能讨论是否已有研究 |
| 其他行业，无知识库 | 1 | [农业机器人](runs/2026-10-29-深度模拟/scenario-05.md) | 明确没有资料、不编论文、不判断该不该入行 | 方向分类没有依据 |
| 其他行业，粘贴虚构笔记 | 1 | [温室笔记](runs/2026-10-29-深度模拟/scenario-05-notes.md) | 拒绝笔记中的三句无出处断言 | 陷阱是测试者故意写的，鉴别能力不能外推 |

总结、反复出现的问题和需要别人才能验证的结论见 [summary.md](runs/2026-10-29-深度模拟/summary.md)。这批记录不能证明 Skill 稳定，也不能代替真实用户测试。

## 2026-10-30 拒绝计算 / 无聊替代

针对上一批里「拒绝做题时没有替代」和「觉得无聊后仍追加加法」的问题，补了低负担替代草稿，并做了两则摘要复盘。记录在 [runs/2026-10-30-refuse-calc/](runs/2026-10-30-refuse-calc/summary.md)。

条件：同一 AI 扮演用户、助手和评价者，没有在 Codex 中加载 Skill。这是自评，不是独立盲测，也不是真实用户反馈。两则整体都是 partial。

| 场景 | 完整对话 | 本轮可见结果 |
|---|---|---|
| 明确拒绝计算 | [scenario-A](runs/2026-10-30-refuse-calc/scenario-A-refuse.md) | 停止计算题，改对照岗位职责（替代 E） |
| 觉得无聊但愿试别的 | [scenario-B](runs/2026-10-30-refuse-calc/scenario-B-bored.md) | 停止加法输入，改比较两段职责（替代 F） |

## 2026-10-30 注意力两层计数

针对 `2026-10-29-深度模拟/scenario-03` 中「分数数组 0 次」易被听成零搬运的问题，在 `experiences.md` 增加含 Query/Key 读取的计数表，并复测一场。记录在 [runs/2026-10-30-attention-count/](runs/2026-10-30-attention-count/summary.md)。

条件：Composer 2.5，同一 AI 自评；未在 Codex 中加载 Skill；未新开文献网页。整体 partial。

| 场景 | 完整对话 | 本轮可见结果 |
|---|---|---|
| 已有 idea（注意力分数） | [scenario-03-rerun](runs/2026-10-30-attention-count/scenario-03-rerun.md) | 引用两层表；12/8 与 4/0 分层说明；用户只认领 11、17 |

## 2026-10-30 自主评估（检索模板 + 六类场景）

新增 [evaluation/retrieval-record-template.md](../evaluation/retrieval-record-template.md)，并在 `SKILL.md` 中指向该模板。记录在 [runs/2026-10-30-自主评估/](runs/2026-10-30-自主评估/summary.md)。

条件：**Composer 2.5**；Skill 基线 SHA `9a829278e75772911864e36fa290c29861307247`；同一 AI 三角色自评；**未**在 Codex 加载 Skill。4a/5a/6b 由维护会话打开 arXiv abs 或搜索页（摘要级），不是 Skill 自动检索。

| 类型 | 次数 | 说明 |
|---|---|---|
| 1 零基础 / 2 方向不明 | 各 1 | 第 2 次未做（优先检索场景） |
| 3 拒绝·无聊·时间 | 2 | [refuse-time](runs/2026-10-30-自主评估/scenario-03-refuse-time.md)、[bored-stop](runs/2026-10-30-自主评估/scenario-03-bored-stop.md) |
| 4 已有 idea | 2 | [有 Skill](runs/2026-10-30-自主评估/scenario-04-existing-attention-with-skill.md) partial；[无 Skill 对照](runs/2026-10-30-自主评估/scenario-04-existing-attention-without-skill.md) 刻意 fail |
| 5 没有 idea | 2 | [有 Skill](runs/2026-10-30-自主评估/scenario-05-no-idea-sram-with-skill.md)；[无 Skill 对照](runs/2026-10-30-自主评估/scenario-05-no-idea-sram-without-skill.md) |
| 6 其他行业 | 2 | [无资料](runs/2026-10-30-自主评估/scenario-06-other-agri-no-kb.md)；[检索+笔记](runs/2026-10-30-自主评估/scenario-06-other-with-search.md) |

整体仍为模拟；**无 pass**；不能把 fail 对照外推为默认模型行为。

## 2026-10-30 角色分离重测

记录在 [runs/2026-10-30-角色分离/](runs/2026-10-30-角色分离/summary.md)。基线 Skill SHA `f09fdb3eeba1b7a88ee16b8329662779d145e6c3`；**未** Codex 加载。

| 场景 | 文件 | 分离程度 | 结果 |
|---|---|---|---|
| 4 已有 idea | [scenario-04-existing-idea-sep](runs/2026-10-30-角色分离/scenario-04-existing-idea-sep.md) | 1–4 轮用户/助手独立子代理；5–8 **同代理代写** | partial |
| 5 没有 idea | [scenario-05-no-idea-sep](runs/2026-10-30-角色分离/scenario-05-no-idea-sep.md) | 1–3 分离；4–7 代写 | partial |
| 6a 无资料 | [scenario-06a-other-no-kb-sep](runs/2026-10-30-角色分离/scenario-06a-other-no-kb-sep.md) | 用户/助手分子代理 8 轮 | partial |
| 6b 笔记+检索 | [scenario-06b-other-with-search](runs/2026-10-30-角色分离/scenario-06b-other-with-search.md) | **8 轮单会话生成**（见文件头） | partial |

与 [2026-10-30-自主评估](runs/2026-10-30-自主评估/summary.md) 对比：**整体档位仍为 partial**；检索 executor 更可追溯，**未**出现 pass 或真实用户验证。

## 2026-10-30 角色分离补测（严格化）

针对上一批 **5–8 / 4–7 轮代写** 与 **6b 单会话**，记录在 [runs/2026-10-30-角色分离-补测/](runs/2026-10-30-角色分离-补测/summary.md)。基线 SHA `ae627f7eda3cd0e582ff25b494d4e475338fa1a6`；**未** Codex 加载。

| 场景 | 文件 | 轮次 | 分离 | 结果 |
|---|---|---|---|---|
| 4 已有 idea | [scenario-04-existing-idea-strict](runs/2026-10-30-角色分离-补测/scenario-04-existing-idea-strict.md) | 10 | 全程双代理 | partial |
| 5 没有 idea | [scenario-05-no-idea-strict](runs/2026-10-30-角色分离-补测/scenario-05-no-idea-strict.md) | 10 | 全程双代理 | partial |
| 6b 笔记+检索 | [scenario-06b-other-with-search-strict](runs/2026-10-30-角色分离-补测/scenario-06b-other-with-search-strict.md) | 10 | 6b 逐轮双代理 | partial |

场景 4 检索 **≤3 篇 abs 且维护者 spot-check**；整体仍 **无 pass**。

## 2026-10-31 自主评估（Skill 默认 ≤3 + 场景 4 无口头上限复测）

记录在 [runs/2026-10-31-自主评估/](runs/2026-10-31-自主评估/summary.md)。基线 `origin/main` SHA `d3da3f7e4df51787124de3bb39c90eea62b3128f`；**Composer 2.5**；**未** Codex 加载。

| 要点 | 说明 |
|---|---|
| Skill 改动 | `SKILL.md` 首次检索默认 ≤3 条；用户要检索时同/下轮给结果（非只确认会去查） |
| **4a 复测** | 用户**未**说「最多 3 篇」；助手子代理仍 **≤3** abs（对照改前 [角色分离 9 篇](runs/2026-10-30-角色分离/scenario-04-existing-idea-sep.md)） |
| 有/无 Skill | 场景 4、5 各 2 场（4a 角色分离；5 同一 AI 自评） |
| 结果 | 仍 **无 pass**；均为模拟 |

## 2026-10-31 自主评估补测（场景 1/2 第 2 次 + 无 Skill 对照）

记录在 [runs/2026-10-31-自主评估-补测/](runs/2026-10-31-自主评估-补测/summary.md)。基线 SHA **`aac9503`**；**Composer 2.5**；**未** Codex 加载。

| 要点 | 说明 |
|---|---|
| 补齐 | 场景 **1、2 各第 2 次**（角色分离）；场景 **1、2、6a** 各 1 场 **无 Skill** 对照 |
| Skill 改动 | 初学者 pacing/术语/未联网就业；`knowledge-pack` 禁止无资料时映射芯片术语与空分类 |
| 改后复测 | 场景 1 就业边界、6a 切换行业；见补测 summary |
| 与上一目录 | [2026-10-31-自主评估](runs/2026-10-31-自主评估/summary.md)（≤3 检索 + 4a 复测）**保留** |
