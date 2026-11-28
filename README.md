# AI 芯片方向探索与科研构思

一个 Codex Skill，给 AI 芯片方向的初学者当对话伙伴：先了解你的背景和目标，再帮你认识方向、做轻量体验，或围绕科研 idea 展开探索。默认面向中国大陆大学生，也可以换成你提供资料的其他行业。

**状态：第一版草稿。** 目前只有 AI 模拟对话，尚未在 Codex 中实测加载，也没有真实用户试用。详见 [STATUS.md](STATUS.md)。

## 能做什么

- **认识方向**：先给一张简明全景，再按你的兴趣、基础、时间和设备逐步聊。
- **体验方向**：做不用买硬件、普通电脑或纸笔就能完成的中文小任务，边做边辨认自己喜欢哪种工作；不想算题时可改成阅读岗位职责或口语对照，说停就停。
- **探索科研 idea**：没有 idea 时按你的条件给少量候选；已有 idea 时沿你的表述收窄、查相近研究、设计初步验证，并整理成可继续核查的卡片。
- **切换行业**：提供文件、网页或论文链接，或在工具可用时让它查资料；它会先说明实际读到了什么。

## 安装

本项目优先面向 Codex，其他 agent 尚未验证。以下步骤**尚未在目标环境实测**：

1. 把 `skills/ai-chip-explorer` 整个文件夹（含 `SKILL.md` 和 `references/`）复制到 Codex 用户级技能目录：Windows 为 `%USERPROFILE%\.codex\skills\ai-chip-explorer`，macOS/Linux 为 `~/.codex/skills/ai-chip-explorer`；设置了 `CODEX_HOME` 时以其下的 `skills` 为准。
2. 目标目录已有同名技能时，先核对内容，不要直接覆盖。
3. 重新打开 Codex 会话，输入 `$ai-chip-explorer` 并描述需求。

续学便条请保存在 Skill 文件夹之外，以免更新或覆盖安装时丢失。

## 起手提示词

```text
$ai-chip-explorer 我是电子信息专业大一，对 AI 芯片感兴趣，但不清楚有哪些方向。请先帮我了解，再设计一个轻量体验。
```

```text
$ai-chip-explorer 我关注矩阵计算的数据搬运，有一个初步想法：……请先了解我的基础和条件，再帮我分析它。
```

```text
$ai-chip-explorer 我想探索机器人领域，附件和链接是我准备的资料。请说明实际读到的内容，并帮我梳理方向。
```

## 局限

- 输出是探索建议，不是就业预测、能力测评或科研创新性证明。
- 就业信息会过期：要核对岗位所在地区和发布时间，一家公司的招聘页不代表整个行业。
- 文献检索范围有限：找不到结果不等于没人研究，也不能保证能发表。
- [案例](cases/README.md)全部是 AI 模拟：由 AI 扮演用户、助手和评价者，没有在 Codex 中加载 Skill，也没有真实用户参与。加载 Skill 的场次整体评价都是「部分通过」，不能说明稳定性或真实效果。

## 案例

[cases/README.md](cases/README.md) 用一张表列出 11 个典型的「痛点 → 回应」，每行链接到完整对话；下面按日期列出全部测试批次。

## 目录

| 路径 | 内容 |
|---|---|
| [skills/ai-chip-explorer/](skills/ai-chip-explorer/SKILL.md) | Skill 本体：主文件和 `references/` 参考资料 |
| [cases/](cases/README.md) | 模拟对话记录与案例索引 |
| [evaluation/](evaluation/README.md) | 量规、角色设定、检索记录模板、真实试跑材料和汇总脚本 |
| [STATUS.md](STATUS.md) | 当前状态与待办 |
| [MAINTENANCE-LOG.md](MAINTENANCE-LOG.md) | 按日期的维护改动与复测记录 |
| [MAINTENANCE-PROMPT.md](MAINTENANCE-PROMPT.md) | 交给 AI 助理的维护提示词 |

## 许可与反馈

采用 [MIT License](LICENSE)。引用或复用外部项目内容前请核对相应许可。发现问题时，请记下问题、使用环境和复现方式，通过本仓库的 Issues 提交。
