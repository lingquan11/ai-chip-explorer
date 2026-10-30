# 文献与资料检索记录模板

维护模拟评估、idea 打磨或换行业查资料时，请按场填写一份记录（可嵌在案例 Markdown 的「检索记录」小节，或另存为 JSON/YAML）。**同一 AI 自评时也要写**，避免把「还没查」写成「查完没有」。

## 何时必须填写

- 用户要求查论文、岗位、行业资料，或助手主动提出检索时。
- 对话里出现具体文献标题、链接、DOI、招聘条目时。
- 即使用户最终没选某个候选方向，只要打开过来源就应记录。

## 单场检索头信息

| 字段 | 说明 |
|---|---|
| `retrieval_id` | 本场唯一标识，如 `2026-10-30-自主评估-s04-run1` |
| `query` | 实际使用的检索式或站点内关键词（写原文，不美化） |
| `databases_or_sites` | 如 arXiv、Google Scholar、用户给的 PDF、招聘页 URL |
| `accessed_at` | 查阅日期与时区，如 `2026-10-30 08:45 Asia/Shanghai` |
| `region_scope` | 就业或政策语境，如「中国大陆校招样本」「全球英文预印本」 |
| `network` | 本场是否真的能打开外链；若不能，写「未联网，以下为空」 |
| `executor` | 谁执行的检索（Skill 会话 / 维护代理 / 角色分离的评价者） |

Skill 默认：首次检索先归档 **≤3 条**来源行；扩大范围须用户明确要求或对话中说明原因（见 `SKILL.md`「科研与证据」）。

## 每条来源（可重复多行）

| 字段 | 说明 |
|---|---|
| `url` | 完整 URL 或 DOI 解析后的链接 |
| `title` | 页面标题或论文名 |
| `read_scope` | **实际读到什么**：仅检索列表标题 / 摘要 / 引言前几段 / 全文 / 岗位职责条目 / 用户笔记某段 |
| `not_read` | 明确未读：全文、附录、代码、实验复现、其他语言版本 |
| `relevance_note` | 与用户问题的关系（相近 / 部分重叠 / 仅背景），**不是**创新性结论 |

## 未能验证项（必填，可为「无」）

列出本场**没有**做到的事，例如：未读全文、未查中文库、未复现实验、未核对发布日期、只一家公司招聘页、检索列表只看了前 3 条。

## 结果为空或很少时怎么写

| 情况 | 允许表述 | 禁止表述 |
|---|---|---|
| 还没检索 | 「尚未检索，不能判断是否有相近工作」 | 「可能还没人做过」 |
| 检索无命中 | 「按该检索式在某库未找到条目；**不等于**证明无人研究」 | 「证明是空白领域」 |
| 只读到摘要 | 「摘要提到 X，是否与你的约束一致**未核对**」 | 「和你的 idea 完全一样/完全不同」 |
| 有限几篇 | 「找到 N 篇部分相关；**未**声称穷尽」 | 「全部相关工作就是这三篇」 |

## 与 idea 卡片、量规的对应

- [idea 卡片](../skills/ai-chip-explorer/references/idea-card.md) 的「已有工作」应能回溯到本模板中的来源行。
- [评价量规](rubric.md) 第 4 项「依据与边界」：无检索记录却出现具体论文名 → 不应判为通过。

## 示例（字段示意，非真实用户）

```yaml
retrieval_id: example-attention-2026-10-30
query: "attention accelerator dataflow memory traffic QK 2024"
databases_or_sites: arXiv search, doi.org
accessed_at: "2026-10-30 08:50 Asia/Shanghai"
region_scope: 英文预印本；用户约束「推理、CPU、两周」尚未逐条对照
network: 有网；打开 2 个 abs 页摘要区
sources:
  - url: https://arxiv.org/abs/2402.07443
    title: The I/O Complexity of Attention...
    read_scope: abs 页摘要与标题
    not_read: 全文、证明、代码
    relevance_note: 讨论 Q/K/V 与 I/O；未核对是否覆盖「不物化分数表」
unverified:
  - 未查 CNKI / 中文会议
  - 未打开 PMLR 正式版
  - 未证明 idea 新颖或陈旧
empty_result_wording: 不适用（有命中）
```

## JSON 片段（可选，便于脚本汇总）

若与 [record-template.json](record-template.json) 一并归档，可在 JSON 中增加 `retrieval_log` 对象，字段名与上表一致；`summarize.py` 当前不校验该字段，仅作人工追溯。
