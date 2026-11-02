# 2026-11-02 自主评估总结

> 维护 run **Composer 2.5**（无更细构建号）。**模拟不代表真实用户效果**；**未在 Codex 加载 Skill**（助手按仓库读 `SKILL.md` + `references/`）。

## 基线

| 项 | 值 |
|---|---|
| 维护开始 `origin/main` SHA | **`e0a5202`** |
| 本轮 Skill 改动 | 禁止对用户暴露 A–G 编号；第二次 boring 停、不轮换第三种；有 idea 时两层计数同轮 + 不因 FlashAttention 否定假设 |
| 日期 | 2026-11-02（Asia/Shanghai） |
| 平台 | Cursor Cloud Agent；可联网；arXiv abs HTTP 200 核实 |

## 场景与次数

| 类型 | 次数 | 文件 | 分离 | 整体 |
|---|---|---|---|---|
| 1 零基础 | 2 | [jargon](scenario-01-jargon-sep.md)、[time-only](scenario-01-time-only-sep.md) | 子代理 | partial ×2 |
| 2 方向不明 | 2 | [reject-verif](scenario-02-reject-verification-sep.md)、[mid-compiler](scenario-02-mid-switch-compiler-sep.md) | 子代理 | partial ×2 |
| 3 拒绝/无聊 | 2 | [refuse-jd](scenario-03-refuse-calc-jd-sep.md)、[double-bored](scenario-03-double-bored-sep.md) | 3a 分离；3b 自评 | partial ×2 |
| 4 已有 idea | 2 | [4a](scenario-04-attention-prior-art-sep.md)、[4b 无 Skill](scenario-04-without-skill-sep.md) | 4a 分离 | partial / **fail** |
| 5 没有 idea | 2 | [textbook](scenario-05-no-idea-textbook-sep.md)、[energy](scenario-05-no-idea-energy-sep.md) | 分离 | partial ×2 |
| 6 其他行业 | 2 | [6a](scenario-06a-agri-no-kb-sep.md)、[6b](scenario-06b-agri-trap-sep.md) | 分离 | partial ×2 |

**合计：** 12 场主测 + **3** 场改后复测 + **1** 场无 Skill 对照（场景 1）。

## 改前 / 改后复测

| 问题 | 改前 | 修改 | 改后 |
|---|---|---|---|
| 对用户说 G/F/A–D（1/3） | [1a](scenario-01-jargon-sep.md) 量规 5/6 partial | `SKILL.md` + `experiences.md` 禁止对用户暴露编号 | [1a retest](scenario-01-jargon-retest-after-fix.md) 5/6 **通过**；[3 retest](scenario-03-refuse-jd-retest-after-fix.md) 量规 5 **通过** |
| 分数层 0 次误解（4） | 历史 [10-29 scenario-03](../../2026-10-29-深度模拟/scenario-03.md) | SKILL 有 idea + experiences 两层同轮 | [4 layer2 retest](scenario-04-layer2-retest-after-fix.md) 量规 5 **通过** |
| 第二次 boring 仍轮换 | 10-29 scenario-02 | experiences 第 2 条 + SKILL 一句 | [3b](scenario-03-double-bored-sep.md) 6 **通过**（改前已符合，本轮写入 Skill 固化） |

## 无 Skill 对照

| 场景 | 有 Skill | 无 Skill | 局限 |
|---|---|---|---|
| 1 术语+拒 JD | 口语对照路径 | [1c partial/5 未通过](scenario-01-without-skill-sep.md) | 同一维护日 |
| 4 检索 | 模板 + ≤2 | [4b fail](scenario-04-without-skill-sep.md) | 脚本化 fail |

## 优先问题汇总

| # | 场景·轮次 | 影响 | 建议文件 | 状态 |
|---|---|---|---|---|
| 1 | 1·5–6 | 用户听不懂内部编号 | `SKILL.md` / `experiences.md` | **已修 + 复测** |
| 2 | 4·计数 | 「0 次」误解零搬运 | `SKILL.md` + experiences 两层 | **已修 + 复测** |
| 3 | 1 无 Skill | 拒 JD 仍推课程 | Skill 无法约束 | 记录对照 |

## 联网与 read_scope

| 场次 | URL | 核实 |
|---|---|---|
| 4a | 2402.07443, 2406.10491 | HTTP 200 |
| 5b | 2111.12885 | HTTP 200 |
| 6b | 2505.12665 | HTTP 200 |

均为 **abs 摘要级**。

## 测试命令（实际执行）

```bash
python3 -m unittest discover -s evaluation -p "test_*.py" -v
```

3 项 OK（见提交时终端输出）。

## 结果档位

- **pass：** 无（整体）
- **partial：** 主测 12 场 + 复测 3 场
- **fail：** 4b 无 Skill 对照

## 未完成 / 下一步

- Codex 安装与自动加载 Skill  
- 四练习学生试跑耗时  
- DeepSeek 适配（不做）  
- 真实用户盲测  

## 完整对话入口

本目录各 `scenario-*.md`。
