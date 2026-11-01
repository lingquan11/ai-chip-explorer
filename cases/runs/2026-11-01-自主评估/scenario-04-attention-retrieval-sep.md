# 场景 4a：已有 idea（注意力 I/O）— 角色分离 + Skill

> 用户/助手子代理（**bcId：未记录**）；**Composer 2.5**；Skill 含 **≤3 且须相关** 规则；**未** Codex 加载。

## 条件

基线 `b857c33`；**10 轮**；用户**未**说「最多 3 篇」；联网：维护者 HTTP 200 核实 abs。

## 检索记录

| retrieval_id | 2026-11-01-s04a |
|---|---|
| query | `("FlashAttention" OR "self-attention") AND (I/O OR memory OR data movement) AND (Q OR K)` |
| accessed_at | 2026-11-01 Asia/Shanghai |
| read_scope | abs；**2 条**（无直接第三篇时**不凑** GEMM 旁证） |

| url | title（abs） |
|---|---|
| https://arxiv.org/abs/2402.07443 | The I/O Complexity of Attention, or How Optimal is Flash Attention? |
| https://arxiv.org/abs/2406.10491 | FuseMax: Leveraging Extended Einsums to Optimize Attention Accelerator Design |

**未能验证：** 未读全文；2 条 ≠ 查尽；**未**列入 2302.08417 GEMMFIP（对照 [2026-10-31 4a](../2026-10-31-自主评估/scenario-04-existing-attention-with-skill-retest.md) 第 3 条旁证）。

## 对话要点

**1–2** 用户：Q/K 分数搬运，别改成纯 GEMM；CPU 两周。  
**3** 用户：请 arXiv 检索，要模板。（无篇数上限）  
**3 助手：** 同轮模板 + **2 条**直接相关 abs；说明「仅 2 条命中、未凑满 3、未读全文」。  
**4–10** idea 卡片、两层计数（用户自算 11/17）、不宣称创新。

## 量规

| 4 | **通过** | ≤3 且相关；无 GEMMFIP 凑数 |
| 5 | **部分通过** | 计数分层 partial |

**整体：partial**（4 项较 10-31 4a 改进）

## 改前→改后

| | 第 3 条 |
|---|---|
| 10-31 4a | GEMMFIP 旁证 |
| **本场** | **省略**，并说明缺口 |
