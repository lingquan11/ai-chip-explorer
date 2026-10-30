# 场景 4：已有 idea（矩阵乘法数据搬运）— 严格角色分离补测

> **分离方式（如实）：**  
> - **第 1–10 轮：** 模拟用户 = 独立子代理（`bc-97a85c8a`）；被测助手 = 独立子代理（`bc-f793e3c4`），仅读 `SKILL.md` + `references/`。  
> - **后半程（6–10 轮）仍由上述两代理分别续写**，未用同一子代理代写双方。  
> - **评价者：** 独立子代理（`bc-13ce3023`），仅对话 + `rubric.md`。

## 条件

| 项 | 值 |
|---|---|
| 日期 | 2026-10-30（Asia/Shanghai） |
| 模型 | Cursor 子代理 **inherit**（维护 run **Composer 2.5**） |
| 基线 `origin/main` SHA | `ae627f7eda3cd0e582ff25b494d4e475338fa1a6` |
| Skill SHA | 同上 |
| Codex 加载 | 否 |
| Persona | `evaluation/personas.md` → **existing-idea**（仅用户子代理可见） |

## 检索记录（第 3 轮，executor = 被测助手子代理）

| 字段 | 内容 |
|---|---|
| retrieval_id | 2026-10-30-角色分离补测-s04 |
| query | `GEMM blocking tiling memory`；站内补充 `GEMM blocking tiling cache` |
| databases_or_sites | arXiv search；下列 abs 页 |
| accessed_at | 2026-10-30 08:30 UTC |
| region_scope | 英文预印本；用户「CPU、一周、256³」**尚未**与每篇实验设定逐条对照 |
| network | 有网；打开 **3** 个 abs 摘要区 |
| executor | 被测助手子代理 bc-f793e3c4 |

| url | title | read_scope | not_read | relevance_note |
|---|---|---|---|---|
| https://arxiv.org/abs/1609.00076 | BLISlab: A Sandbox for Optimizing GEMM | abs 摘要 | 全文、代码 | 部分重叠：cache 层级上分块与 BLIS 思路 |
| https://arxiv.org/abs/2208.08088 | AutoTSMM: … Tall-and-Skinny MM on CPUs | abs 摘要 | 全文 | 部分重叠：cache blocked；形状偏 TSMM |
| https://arxiv.org/abs/2302.08417 | GEMMFIP: Unifying GEMM in BLIS | abs 摘要 | 全文 | 背景：Goto/BLIS blocking |

**维护者 spot-check（2026-10-30）：** 上述 3 个 abs HTTP **200**。

**未能验证：** 未读全文；未查非 arXiv 经典文献；**3 篇 ≠ 穷尽**；未证明新颖或陈旧。

## 完整对话（10 轮）

**1 用户：** 我有个 idea：减少矩阵乘法的数据搬运，也许能提升 AI 加速器效率。能帮我打磨吗？

**1 助手：** 理解成「少搬数据」提升效率，但具体改哪一段还不清楚。先问：最想减少哪类搬运（DRAM↔片上、cache 间、片间、重复读权重/激活）？

**2 用户：** 更像 GEMM 时权重和激活在 cache 和主存之间来回拉；只有普通 CPU，约一周；想先搞清 L1/L2/L3 与 DRAM 哪段最拖后腿，让数据在 cache 多复用几次。

**2 助手：** 对齐 CPU 与加速器在「复用」概念上相近、机制上不同；一周可做 naive vs 分块 + perf 的小对照。问：Linux/C++/perf 是否可用？

**3 用户：** Linux、C++、`perf` 可用。请 arXiv 检索相近工作，按检索记录模板写，**最多 3 篇** abs；附 idea 卡片草稿选项。

**3 助手：** 给出 `retrieval_id=2026-10-30-角色分离补测-s04` 与上表 3 篇；idea 卡片草稿（256³、naive vs blocked、perf 指标）；声明未读全文、不等于穷尽。

**4 用户：** 检索没命中是否等于没人做？

**4 助手：** **不等于。** 列表短常因关键词/库单一；CPU GEMM 分块在教科书与 BLIS 路线中大量存在。

**5 用户：** 选 M=N=K=256、float、naive vs 分块；今天不跑，只定 checklist。

**5 助手：** 环境表、正确性、perf 事件集合、两版 GEMM + 空结果表、讨论占位；Done 定义=代码+README+空表。

**6 用户：** 定 float。idea 卡片「不同点」怎么写不吹牛？

**6 助手：** 相同点/不同点表：工业 BLIS vs 你「256³、自写简单分块、perf 证据链」；禁止写「首次发现分块」。

**7 用户：** 今天不跑，对照 checklist 是否齐全（warmup、`-O3`、tile 变量等）。

**7 助手：** Step 0–5 最小执行顺序与 perf 命令形态；分块参数占位 64 或 32³。

**8 用户：** BLIS 成熟是否说明我的 idea 没价值？

**8 助手：** 分开「文献已说清的分块」与「本机对照测量+解释」；允许写「在成熟背景下做可复现测量」，禁止 claim 发明分块。

**9 用户：** 检索与清单已存，今天结束，谢谢。

**9 助手：** 收束：float、256³、边界清楚；未宣称创新。

**10 用户：** 结论能否留一句「对加速器减少搬运有启发」？如何限定？

**10 助手：** 给 Conclusion 模板：CPU 计数**不能**直接换算 NPU；可共用「复用/流量」词汇但机制须分开论证。

## 评价者结论（bc-13ce3023）

| 整体 | **partial** |
|---|---|
| 依据与边界 | **通过**（3 篇核实；体量克制） |
| 相关路径 | **通过** |
| 可执行与反馈 | **部分通过**（清单有，未跑实验） |
| 过程 | **通过**（10 轮全程双代理，无代写） |

对比 [2026-10-30-角色分离](../2026-10-30-角色分离/scenario-04-existing-idea-sep.md)：该场 5–8 轮代写且第 3 轮 **9 篇**并列；本场 **3 篇 + 全轮分离**，依据项升档，整体仍 partial。
