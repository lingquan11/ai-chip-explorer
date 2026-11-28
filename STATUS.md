# 项目状态

更新：2026-11-27。本页只写当前状态和待办；每次改动的经过、证据来源和验证命令按日期记在 [MAINTENANCE-LOG.md](MAINTENANCE-LOG.md)。没有实际运行过的内容不写成已验证。

## 范围

第一版：Codex 优先；AI 芯片方向全景、轻量体验与低负担替代入口、科研 idea 辅助、按需学习辅助、可替换的行业资料、手动模拟评估包和中文说明。其他 agent（含 DeepSeek）和更多行业留待以后。

## 当前状态

| 项目 | 状态 |
|---|---|
| Skill 文件 | `SKILL.md` 加 12 份 `references/`。元数据曾用 skill-creator `quick_validate.py` 检查通过；2026-11-27 检查仓库内 Markdown 相对链接无断链。这只说明文件格式，不说明对话效果。 |
| Codex 安装、自动发现、真实对话 | 未测。[evaluation/codex-probe.md](evaluation/codex-probe.md) 第一阶段探针全部 `not_run`。 |
| 模拟测试 | 2026-10-29 至 11-02 共 12 批，索引见 [cases/README.md](cases/README.md)。加载 Skill 的场次整体都是 partial，没有 pass；均未在 Codex 中加载，没有真实用户。 |
| 轻量体验与学习辅助 | 步骤、依赖和实际耗时都没有真人试跑；学习辅助只有脚本化或静态核对。 |
| 真实用户试跑 | 材料已备（[evaluation/real-trial/](evaluation/real-trial/PROTOCOL.md)），尚未试跑。 |
| 评估脚本 | 2026-11-27：`python3 -m unittest discover -s evaluation -p "test_*.py" -v` 4 项通过；`python3 evaluation/check-counting-probes.py` 通过（9 个计数、8 个教学合成探针）。只检验脚本本身，不代表 Skill 效果。 |
| 外部行业资料 | 不同文件、网页、论文和权限条件下的实际读取能力未测。 |
| 许可证 | MIT（[LICENSE](LICENSE)）。复用外部内容前仍需核对其许可。 |

## 待办

1. 在 Codex 中实际安装，跑 [codex-probe.md](evaluation/codex-probe.md) 第一阶段：能否发现和加载 Skill、能否按小节读取参考资料。
2. 按 [real-trial/PROTOCOL.md](evaluation/real-trial/PROTOCOL.md) 找真实学生试跑；试跑前先提交模拟摩擦快照并记下提交号。
3. 让真人试做轻量体验和学习辅助，记录能否跟做、实际耗时。
4. 在联网条件下测试论文与岗位检索，按[检索记录模板](evaluation/retrieval-record-template.md)记来源、时间、覆盖范围和无法验证的内容。
5. 独立复核：计数模型的第三路推导与语义评审；数据旅程的两次模拟和独立评审；反例题库 CE-04 改假设后的 10 与 6（待零醛复核）。
6. 补全[来源台账](skills/ai-chip-explorer/references/sources-ledger.md)的待补项（含 arXiv 2111.12885、2505.12665 的标题）；核对 SCALE-Sim 官方文档后试做对账卡。
7. 仓库还没有覆盖：用户追问内部编号含义时怎么回答。
8. 每月复查一次招聘页（如墨芯「加入我们」页）是否仍无发布日期、内容是否变化。
9. 待零醛决定：矩阵乘辅助是否保留 blocked 对照、是否扩大规模。
10. 以后：其他 agent（含 DeepSeek）适配，更多行业资料。
