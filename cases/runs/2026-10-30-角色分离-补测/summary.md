# 2026-10-30 角色分离补测总结

> 对照 [2026-10-30-角色分离](../2026-10-30-角色分离/summary.md)（**部分轮次代写 / 6b 单会话**）与 [2026-10-30-自主评估](../2026-10-30-自主评估/summary.md)（同一 AI 三角色自评）。**不删**历史 cases。

## 基线

| 项 | 值 |
|---|---|
| 起始 `origin/main` SHA | `ae627f7eda3cd0e582ff25b494d4e475338fa1a6` |
| Skill SHA | 同上 |
| 模型 | 子代理 **inherit**（维护 run **Composer 2.5**） |
| Codex 加载 Skill | 否 |

## 分离是否真正实现

| 场景 | 用户子代理 | 助手子代理 | 评价者 | 后半程 |
|---|---|---|---|---|
| **4 已有 idea** | bc-97a85c8a（1–10） | bc-f793e3c4（1–10） | bc-13ce3023 | **6–10 仍双代理**，无代写 |
| **5 没有 idea** | bc-1ffa228e（1–10） | bc-7bbe8298（1–10） | bc-13ce3023 | **4–10 仍双代理** |
| **6b 笔记+检索** | bc-5d3760f8（1–10） | bc-3e400e1b（1–10） | bc-13ce3023 | **逐轮双代理**（非单会话） |

**交接规则：** 用户子代理仅 `evaluation/personas.md`（6b 含用户自拟笔记 brief）；助手仅 `SKILL.md` + `references/`；评价者仅对话 + `rubric.md`。

## 场次与检索

| 文件 | 轮次 | 联网 URL（维护者核实） | read_scope | 整体 |
|---|---|---|---|---|
| [scenario-04-existing-idea-strict.md](scenario-04-existing-idea-strict.md) | 10 | 1609.00076, 2208.08088, 2302.08417 | abs；**≤3 篇** | partial |
| [scenario-05-no-idea-strict.md](scenario-05-no-idea-strict.md) | 10 | 2106.10499, 2409.13625, 2302.07594 | abs | partial |
| [scenario-06b-other-with-search-strict.md](scenario-06b-other-with-search-strict.md) | 10 | 2407.13304, 2505.12665 | abs | partial |

## 与上一批对比

| 维度 | 角色分离（上一批） | 本批补测 | 变化 |
|---|---|---|---|
| 4/5 后半程 | 同代理代写 | 全程双代理 | **过程可信度↑** |
| 4 检索体量 | 9 篇并列 | **上限 3 篇** + spot-check | **依据项↑**（仍 partial） |
| 6b 生成方式 | 8 轮单会话 | 10 轮逐轮双代理 | **执行方式对齐 brief** |
| 整体 pass | 无 | 无 | **无变化** |
| Skill 代码 | 无改 | 无改 | 高频「检索堆砌」用 **流程约束** 缓解，未改 SKILL |

## 自主评估对照

- **4a/5a/6b** 自评批：executor 混同、4a 易长列表 → 本批 **executor 与子代理 id 可追溯**，6b **双 abs**。
- **无 Skill 对照**（4b/5b）：本批仍未做分离 fail 对照。
- **结论档位：** 仍为 **partial**；分离 **未** 升级为 pass 或真实用户验证。

## 代码改动

**无。** 场景 4 检索堆砌在上一批已记录；本批用「最多 3 篇 + 核实」验证可执行，**不**据此改 SKILL（避免未在 Codex 路径验证的硬编码）。

## 测试

- `python3 -m unittest discover -s evaluation -p "test_*.py" -v`：**3 OK**
- Markdown 相对链接：仓库内 `*.md` 相对路径抽检 **OK**（含本目录链至 `evaluation/`、`../2026-10-30-角色分离/`）

## 未完成

- 场景 **6a** 无资料分离重跑（本批优先 6b brief）；Codex 加载；角色分离下 **无 Skill** 对照；完整 transcript 逐字归档（本场为摘要体 + 子代理 id 可追溯）。

## 局限

仍为 **模拟**；评价者读摘要体 transcript；arXiv **仅 abs**；不能把 partial 写成真实用户或稳定性证明。
