# 2026-11-01 自主评估总结

> 维护 run **Composer 2.5**（无更细构建号）。**模拟不代表真实用户效果**；**未在 Codex 加载 Skill**（助手子代理按仓库读 `SKILL.md` + `references/`）。

## 基线

| 项 | 值 |
|---|---|
| 维护开始 `origin/main` SHA | **`b857c33`** |
| 本轮 Skill 改动 | `SKILL.md`：≤3 **须与 problem 直接相关**、旁证须同轮说明；体验偏好指向 **G**；强化不得从单次体验/粗计时推适合性。`references/experiences.md`：新增 **替代体验 G**（拒手算且拒 JD 时） |
| 日期 | 2026-11-01（Asia/Shanghai） |
| 平台 | Cursor Cloud Agent；宿主可联网；检索场次维护者 HTTP 核实 abs |

## 场景与次数

| 类型 | 次数 | 文件 | 分离 | 整体 |
|---|---|---|---|---|
| 1 零基础 | 2 | [misinterest](scenario-01-beginner-misinterest-sep.md)、[refuse-buy](scenario-01-beginner-refuse-buy-sep.md) | 子代理 | partial ×2 |
| 2 方向不明 | 2 | [course-not-pref](scenario-02-course-not-pref-sep.md)、[mid-change](scenario-02-mid-change-target-sep.md) | 子代理 | partial ×2 |
| 3 拒绝/无聊/时间 | 2 | [refuse-calc+jd](scenario-03-refuse-calc-and-jd-sep.md)、[bored-A](scenario-03-bored-on-A.md) | 3a 分离；3b 自评 | partial ×2 |
| 4 已有 idea | 2 | [4a Skill](scenario-04-attention-retrieval-sep.md)、[4b 无 Skill](scenario-04-attention-without-skill-sep.md) | 4a 分离 | partial / **fail** |
| 5 没有 idea | 2 | [textbook](scenario-05-no-idea-textbook-sep.md)、[switch-precision](scenario-05-no-idea-switch-precision-sep.md) | 分离 | partial ×2 |
| 6 其他行业 | 2 | [6a](scenario-06a-agri-no-kb-sep.md)、[6b](scenario-06b-agri-with-search-sep.md) | 分离 | partial ×2 |

**合计：** 12 场主测 + 2 场改后复测 + 1 场无 Skill 对照（场景 3）。

## 改前 / 改后复测

| 问题 | 改前 | 修改 | 改后 |
|---|---|---|---|
| 拒 JD 后无低负担路径（3） | [10-31 3a](../2026-10-31-自主评估/scenario-03-refuse-time.md) partial | **G** + SKILL 指向 | [3a 本场](scenario-03-refuse-calc-and-jd-sep.md) 量规 6 **通过**；[retest](scenario-03-refuse-jd-retest-after-fix.md) |
| 检索第 3 条 GEMMFIP 旁证过宽（4） | [10-31 4a](../2026-10-31-自主评估/scenario-04-existing-attention-with-skill-retest.md) | SKILL 相关性与不凑数 | [4a 本场](scenario-04-attention-retrieval-sep.md) **2 条**；[retest](scenario-04-retrieval-relevance-retest-after-fix.md) 量规 4 **通过** |
| 单次体验推适合性（2 无 Skill 历史） | 10-31 补测 without-skill | SKILL 强化一句 | 本场 2a **未**从一次 C 推适合（量规 4 通过） |

## 无 Skill 对照

| 场景 | 有 Skill | 无 Skill | 局限 |
|---|---|---|---|
| 3 拒 JD | **G** 口语对照 | [without-skill](scenario-03-refuse-jd-without-skill-sep.md) 推验证视频；量规 5 **未通过** | 同一维护日；**不等于**默认模型 |
| 4 检索 | 模板 + ≤2 相关 | [4b fail](scenario-04-attention-without-skill-sep.md) | 刻意 fail 脚本 |

## 优先问题汇总

| # | 场景·轮次 | 影响 | 建议文件 | 状态 |
|---|---|---|---|---|
| 1 | 3·拒 JD | 用户无法继续低负担探索 | `experiences.md` **G** | **已修 + 复测** |
| 2 | 4·第 3 条检索 | 误导「查尽」或题不对 | `SKILL.md` 相关性 | **已修 + 复测** |
| 3 | 3·拒 JD 无 Skill | 仍推课程/热门方向 | Skill 无法约束无 Skill | 记录对照；Codex 加载待测 |

## 联网与 read_scope

| 场次 | URL | 核实 |
|---|---|---|
| 4a | 2402.07443, 2406.10491 | HTTP 200 |
| 5b | 2111.12885 | HTTP 200 |
| 6b | 2505.12665 | HTTP 200 |

均为 **abs 摘要级**，非全文。

## 测试命令（实际执行）

```bash
python3 -m unittest discover -s evaluation -p "test_*.py" -v
```

3 项 OK。

## 结果档位

- **pass：** 无（整体）
- **partial：** 主测 11 场 + 复测 2 场
- **fail：** 4b 无 Skill 刻意对照

## 未完成 / 下一步

- Codex 安装与自动加载 Skill  
- 四练习学生试跑耗时  
- DeepSeek 适配（本轮不做）  
- 真实用户盲测  

## 完整对话入口

本目录各 `scenario-*.md`。
