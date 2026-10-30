# 场景 4a 复测：已有 idea（注意力）— **加载 Skill（含 ≤3 条规则）**

> **角色分离（用户 / 助手）。** 评价者为维护代理（Composer 2.5）。**模拟用户全程未说「最多 3 篇」**，检验 Skill 自克制 vs [2026-10-30-角色分离](../2026-10-30-角色分离/scenario-04-existing-idea-sep.md) 无提示时 **9 篇并列**。

## 条件

| 项 | 值 |
|---|---|
| 起始 `origin/main` SHA | `d3da3f7e4df51787124de3bb39c90eea62b3128f` |
| Skill 改动 | 本分支 `SKILL.md`「科研与证据」：**首次检索默认 ≤3 条** + 同/下轮给结果 |
| 模型 | 用户子代理 **Composer 2.5** `bc-d2d270f3`；助手子代理 **Composer 2.5** `bc-52794730` |
| Codex 加载 Skill | **否** |
| 联网 | 维护者 HTTP 200 核实 abs：2402.07443、2406.10491、2302.08417 |

## 检索记录

| 字段 | 内容 |
|---|---|
| retrieval_id | 2026-10-31-自主评估-s04a-retest |
| query | `("self-attention" OR attention) AND ("I/O" OR fusion OR tile OR FlashAttention)` 等 |
| accessed_at | 2026-10-31 Asia/Shanghai |
| read_scope | abs；**3 条**（非用户口头上限，来自 Skill 默认） |
| executor | 助手子代理；维护者 spot-check URL |

| url | title（abs 页） | read_scope |
|---|---|---|
| https://arxiv.org/abs/2402.07443 | The I/O Complexity of Attention, or How Optimal is Flash Attention? | abs |
| https://arxiv.org/abs/2406.10491 | FuseMax: Leveraging Extended Einsums to Optimize Attention Accelerator Design | abs |
| https://arxiv.org/abs/2302.08417 | GEMMFIP: Unifying GEMM in BLIS | abs（旁证 CPU pack；**非** attention 专用，助手已声明） |

**未能验证：** 未读全文；3 条 **不等于** 查尽；2302.08417 与用户「别偷换 GEMM」需人工判断是否过度引用。

## 完整对话（10 轮，摘要体 + 子代理原文）

**1 用户：** 想在注意力里算 Q/K 点积分数时少做数据搬运，别换成普通 GEMM。  
**1 助手：** 保留题目；确认是否物化整张分数表、推理/训练与设备。  
**2 用户：** 推理；CPU 两周；倾向不物化整张 Q–K 分数表。  
**2 助手：** 约束记下；可纸面计数或查相近工作。  
**3 用户：** 请 arXiv 检索 attention、Q/K、访存或 I/O 相近工作，按模板记，别把题改成纯 matmul。（**未提篇数上限**）  
**3 助手：** 首轮默认 **≤3 条** abs + 完整检索头信息；见上表。  
**4 用户：** 找到了什么？标题和记录能对上吗？  
**4 助手：** 对照 2402.07443 / 2406.10491 为 attention I/O 与 fusion 线；2302.08417 仅 CPU pack 旁证；未读全文、不等于查尽。  
**5–10 用户/助手：** idea 卡片、两层计数（用户自算 11/17）、结束；助手未宣称创新或发表前景。

## 量规（评价者）

| 依据与边界 | **通过** | 3–4：≤3 条 + 模板 + 边界表述；**无用户口头上限** |
| 可执行与反馈 | 部分通过 | 两层计数用户认领 11/17；未独立重数第二层 |
| 整体 | **partial** | 分离未升级为 pass；GEMMFIP 作第 3 条略宽 |

## 对照（修改前 → 修改后）

| 批次 | 用户是否说「最多 3 篇」 | 助手检索体量 |
|---|---|---|
| [角色分离 2026-10-30](../2026-10-30-角色分离/scenario-04-existing-idea-sep.md) | **否** | **9 篇**并列 |
| [补测 strict](../2026-10-30-角色分离-补测/scenario-04-existing-idea-strict.md) | **是** | ≤3 + spot-check |
| **本场 4a 复测** | **否** | **≤3**（Skill 默认） |
