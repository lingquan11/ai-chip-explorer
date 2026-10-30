# 2026-10-30 自主评估总结

> **同一 AI 三角色自评。** 模拟用户、被测助手、评价者均为 **Composer 2.5**（本 run cloud run-info）。存在自评偏差；**未在 Codex 加载 Skill**；**不是**真实用户反馈或独立盲测。

## 基线

| 项 | 值 |
|---|---|
| 维护开始 `origin/main` SHA | `9a829278e75772911864e36fa290c29861307247` |
| Skill 文本基线 | 同上（含 PR #7/#8 后的 experiences 与 SKILL 检索指引） |
| 日期 | 2026-10-30（Asia/Shanghai） |
| Codex 加载 Skill | **否**（预期否） |

## 本轮代码 / 文档改动

1. **A. 检索记录模板**：新增 [evaluation/retrieval-record-template.md](../../../evaluation/retrieval-record-template.md)；`evaluation/README.md`、`SKILL.md`「科研与证据」增加引用。
2. **B. 未改** `references/` 主流程（模拟未暴露比模板更高频的新问题；拒绝计算/注意力表已在 2026-10-30 前序 PR 落地）。

## 联网与实际打开的 URL

| 场次 | URL | 阅读范围 |
|---|---|---|
| 4a | https://arxiv.org/abs/2402.07443 , https://arxiv.org/abs/2406.10491 | abs 摘要级 |
| 5a | https://arxiv.org/abs/2111.12885（经 arXiv 搜索 `SRAM tiling GEMM accelerator`） | 搜索结果摘要 + abs 列表信息 |
| 6b | https://arxiv.org/abs/2505.12665（经搜索 `agricultural robot leaf occlusion vision`） | 搜索结果摘要级 |
| 3a/3b/6a/1a/2a | 无新打开页面 | — |

Google Scholar 在维护环境返回 429，**未**使用；已写在 5a 局限中。

## 场景覆盖（6 类 × 目标 2 次）

| 类型 | 计划 | 实际文件 | 次数 | 备注 |
|---|---|---|---|---|
| 1 零基础 | 2 | [01-beginner-1](scenario-01-beginner-1.md) | **1** | 第 2 次未做（优先检索场景） |
| 2 方向不明 | 2 | [02-undecided-1](scenario-02-undecided-1.md) | **1** | 第 2 次未做（同上） |
| 3 拒绝/无聊/时间 | 2 | [03-refuse-time](scenario-03-refuse-time.md)、[03-bored-stop](scenario-03-bored-stop.md) | 2 | 8–10 轮 |
| 4 已有 idea | 2 | [04a with Skill](scenario-04-existing-attention-with-skill.md)、[04b without Skill](scenario-04-existing-attention-without-skill.md) | 2 | 4a 用模板检索；4b 刻意 fail 对照 |
| 5 没有 idea | 2 | [05a with Skill](scenario-05-no-idea-sram-with-skill.md)、[05b without Skill](scenario-05-no-idea-sram-without-skill.md) | 2 | 5a 有 arXiv 记录 |
| 6 其他行业 | 2 | [06a 无资料](scenario-06-other-agri-no-kb.md)、[06b 检索+笔记](scenario-06-other-with-search.md) | 2 | 6b 打开 2505.12665 |

## Skill 对照（有 / 无 Skill）

| 场景 | 有 Skill | 无 Skill | 结论（仅本批模拟） |
|---|---|---|---|
| 已有 idea | 4a **partial** | 4b **fail** | 模板+边界表述可复现；无 Skill 脚本故意违规 |
| 没有 idea | 5a **partial** | 5b **fail** | 同上 |

**未执行：** 零基础/方向不明/其他行业无资料的「无 Skill」对照（时间优先检索与 3/4/6）。

## 已实现 / 已验证 / 仅模拟 / 待办

| 状态 | 内容 |
|---|---|
| **已实现** | 检索记录模板入仓；SKILL 指向模板；10 场自主评估 Markdown + 本 summary |
| **已验证** | `python3 -m unittest discover -s evaluation -p "test_*.py" -v` 3 项通过（汇总工具）；维护时 `git fetch` 与 origin/main SHA |
| **仅模拟未验证** | 全部对话与量规；4a/5a/6b 检索为 Composer 维护会话打开，非 Codex Skill 自动行为 |
| **已知待办** | 每类第 2 次中的 1/2 未完成；角色分离盲测；Codex 加载；四练习学生试跑；Scholar 429 下的备用检索渠道；招聘页发布日期复查 |

## 复测（改动 A）

| 改动 | 原问题 | 复测 | 相近场景 |
|---|---|---|---|
| 检索模板 + SKILL 一句 | STATUS：缺模板；04/05 未检索 | [4a](scenario-04-existing-attention-with-skill.md) 填完整检索表 | [5a](scenario-05-no-idea-sram-with-skill.md) |

旧记录（2026-10-29 scenario-03/04）**未改**。

## 量规汇总

- **partial**：4a、5a、3a、3b、6a、6b、1a、2a（同一 AI 自评，证据见各文件）
- **fail**：4b、5b（刻意无 Skill 对照，不推断默认模型行为）
- **pass**：无（缺独立评价者与真实用户）

## 反复可见点（本批）

- 有 Skill + 模板时，检索轮能写 URL、日期、read_scope、unverified（4a、5a、6b）。
- 无 Skill 对照出现「无人做过」「发顶会」类表述（4b、5b）— **脚本化**，非实测。
- 类型 3 仍 **partial**：时间不够时虽停题，用户拒绝招聘替代后仍缺其他低负担路径（3a）。

## 未做

- DeepSeek 适配；删除历史 cases；force-push；把模拟写成真实用户效果。
