# 2026-10-31 自主评估总结

> 维护 run **Composer 2.5**。场景 **4a** 为**角色分离**（用户 `bc-d2d270f3` / 助手 `bc-52794730`）；其余场次为**同一 AI 三角色自评**。存在自评偏差；**未在 Codex 加载 Skill**；**不是**真实用户或独立盲测。

## 基线

| 项 | 值 |
|---|---|
| 维护开始 `origin/main` SHA | `d3da3f7e4df51787124de3bb39c90eea62b3128f` |
| 本轮 Skill 改动 | `SKILL.md`「科研与证据」：**首次检索默认 ≤3 条**；用户要检索时**同/下轮**给模板与条目；[retrieval-record-template.md](../../../evaluation/retrieval-record-template.md) 一句默认 ≤3 |
| 日期 | 2026-10-31（Asia/Shanghai） |
| Codex 加载 Skill | **否** |

## 代码 / 文档改动（1–3 处）

1. **A（必须）** `skills/ai-chip-explorer/SKILL.md`：科研与证据段 ≤3 默认 + 反空转一句。  
2. **A 补充** `evaluation/retrieval-record-template.md`：默认 ≤3 来源行一句（不堆 SKILL）。  
3. **B（可选）** 同轮给结果：已并入 SKILL 一句；未另改 references。

## 联网与实际 URL

| 场次 | URL | 核实 |
|---|---|---|
| 4a | 2402.07443, 2406.10491, 2302.08417 | 维护者 HTTP 200 |
| 5a | 2111.12885 | HTTP 200 |
| 6b | 2505.12665 | HTTP 200 |
| 其余 | 无新打开 | — |

**read_scope：** 均为 abs 摘要级，非全文。

## 场景覆盖

| 类型 | 次数 | 文件 |
|---|---|---|
| 1 零基础 | 1 | [01-beginner-1](scenario-01-beginner-1.md) |
| 2 方向不明 | 1 | [02-undecided-1](scenario-02-undecided-1.md) |
| 3 拒绝/无聊/时间 | 2 | [03-refuse-time](scenario-03-refuse-time.md)、[03-bored-stop](scenario-03-bored-stop.md) |
| 4 已有 idea | 2 | [4a 有 Skill 复测](scenario-04-existing-attention-with-skill-retest.md)、[4b 无 Skill](scenario-04-existing-attention-without-skill-retest.md) |
| 5 没有 idea | 2 | [5a](scenario-05-no-idea-sram-with-skill.md)、[5b](scenario-05-no-idea-sram-without-skill.md) |
| 6 其他行业 | 2 | [6a](scenario-06-other-agri-no-kb.md)、[6b](scenario-06-other-with-search.md) |

## 复测关键：场景 4 **无**「最多 3 篇」用户提示

| 对照 | 用户口头上限 | 助手行为 |
|---|---|---|
| [2026-10-30-角色分离 s04](../2026-10-30-角色分离/scenario-04-existing-idea-sep.md)（改 SKILL 前） | 否 | **9 篇** |
| [2026-10-30-角色分离-补测 strict](../2026-10-30-角色分离-补测/scenario-04-existing-idea-strict.md) | **是** | ≤3 |
| **本场 4a**（改 SKILL 后） | **否** | **≤3** + 模板（子代理；仍 partial） |

## Skill 有 / 无对照

| 场景 | 有 Skill | 无 Skill | 本批执行 |
|---|---|---|---|
| 4 已有 idea | 4a partial | 4b fail | **已做**（4a 分离） |
| 5 没有 idea | 5a partial | 5b fail | **已做**（同一 AI 自评） |
| 1/2/6a | — | — | **未做**无 Skill 分离对照 |

## 已实现 / 已验证 / 仅模拟 / 待办

| 状态 | 内容 |
|---|---|
| **已实现** | SKILL ≤3 + 反空转；模板一句；本目录 11 场 + summary |
| **已验证** | `python3 -m unittest discover -s evaluation -p "test_*.py" -v` 3 OK；`git fetch` + origin/main SHA；列出的 abs HTTP 200 |
| **仅模拟** | 除 4a 外均为同一 AI 自评；Skill 行为非 Codex 自动加载 |
| **待办** | 1/2 各类第 2 次；Codex 加载；6a/1/2 无 Skill 分离；DeepSeek 适配不做；真实用户 |

## 量规汇总

- **partial**：4a、5a、3a、3b、6a、6b、1a、2a  
- **fail**：4b、5b（刻意无 Skill）  
- **pass**：无  

## 测试命令

```bash
python3 -m unittest discover -s evaluation -p "test_*.py" -v
```

## 未做

DeepSeek 适配；删历史 cases；force-push；把模拟写成真实用户效果。
