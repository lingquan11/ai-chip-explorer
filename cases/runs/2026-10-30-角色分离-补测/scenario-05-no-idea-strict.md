# 场景 5：没有 idea — 严格角色分离补测

> **分离方式：** 第 **1–10** 轮用户（`bc-1ffa228e`）/ 助手（`bc-7bbe8298`）独立子代理续写；**无**同代理代写。评价者 `bc-13ce3023`。

## 条件

| Skill SHA | `ae627f7eda3cd0e582ff25b494d4e475338fa1a6` |
| Persona | **no-idea**（仅用户子代理） |
| Codex | 否 |

## 检索记录（第 4 轮助手输出，executor = bc-7bbe8298）

| retrieval_id | 2026-10-30-角色分离补测-s05 |
|---|---|
| query | `tiling GEMM on-chip dataflow accelerator` |
| accessed_at | 2026-10-30 Asia/Shanghai |
| network | 有网；**3** abs 已打开核实 |

| url | title | read_scope |
|---|---|---|
| https://arxiv.org/abs/2106.10499 | Evaluating Spatial Accelerator Architectures with Tiled MM | abs |
| https://arxiv.org/abs/2409.13625 | LoopTree: Fused-layer Dataflow Accelerator Design Space | abs |
| https://arxiv.org/abs/2302.07594 | GEMM for deep learning inference on Xilinx Versal | abs |

**spot-check：** 2106.10499、2409.13625、2302.07594 HTTP **200**（2026-10-30）。

**unverified：** 未读全文；OpenBLAS/BLIS **未**在本场 retrieval 中打开；3 篇 ≠ 穷尽。

## 完整对话（10 轮，摘要体）

**1–2 用户/助手：** 无 idea 开场；用户读博、EE 大二、两周笔记本、倾向 GEMM 分块与片上存储；助手给两候选并确认方向。

**3 用户：** 请 arXiv 检索 GEMM tiling/dataflow，模板记录，最多 3 篇 abs。

**3 助手：** 确认检索式；下轮给出记录（实际在第 4 轮助手一并输出检索表）。

**4 用户：** 选纯 GEMM tiling；承认可能与 2106.10499 重叠。

**4 助手：** 完整检索表（上）；与 2106.10499 关系「主题相近、对象可能不同—待读全文」。

**5 用户：** 写一句 proposal 研究问题，标注待读全文。

**5 助手：** idea 卡片草稿 + proposal 一句（纸面 tile 读入次数；不声称超越已有 tiled GEMM 研究）。

**6 用户：** 今天不做脚本；定下周手算 tile 对比计划。

**6 助手：** 4×4 GEMM、缓冲容量 B、慢层读入计数规则；两组 tile 对比步骤。

**7 用户：** 检索很少是否等于空白？

**7 助手：** 检索边界表（允许/禁止表述）；强调未读全文不能判新颖。

**8 用户：** 和 OpenBLAS 差距大，两周手算是否没意义？

**8 助手：** OpenBLAS **未**在本场 retrieval 核实；纸面计数与库优化「同族不同对象」；不必为像科研先接库。

**9–10 用户/助手：** 感谢结束；用户确认下周仅纸面计数；助手收束 retrieval_id、待读全文、不宣称新颖。

## 评价者结论

**partial**（路径与检索可追溯；OpenBLAS 边界已写清；无跑通/无真实用户）。对比 [角色分离批 5](../2026-10-30-角色分离/scenario-05-no-idea-sep.md)：**4–7 轮代写已消除**；对比 [自主评估 5a](../2026-10-30-自主评估/scenario-05-no-idea-sram-with-skill.md)：executor 更可区分，整体档位不变。
