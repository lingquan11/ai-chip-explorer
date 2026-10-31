# 2026-10-31 自主评估补测总结

> 维护 run **Composer 2.5**（`bc-c4dc0d29`）。**模拟不代表真实用户效果**；除标注「角色分离」场次外，评价者与对话生成仍可能在同一维护会话中完成，存在偏差。**未在 Codex 加载 Skill**。

## 基线

| 项 | 值 |
|---|---|
| 维护开始 `origin/main` SHA | **`aac9503`**（PR #16 后 HEAD） |
| 本轮 Skill 改动 | `SKILL.md` 起点段：时间紧不读整表、术语改口语、未联网就业边界、不因课程推验证；`references/knowledge-pack.md`：无资料时不映射芯片术语、不抛空分类 |
| 日期 | 2026-10-31（Asia/Shanghai） |
| 与同日目录关系 | [2026-10-31-自主评估](../2026-10-31-自主评估/summary.md) 已含 ≤3 检索与场景 4 无提示复测；**本目录为补测**，不覆盖该目录 |

## 场景与次数

| 类型 | 次数 | 文件 | 分离 | 整体 |
|---|---|---|---|---|
| 1 零基础 | 第 2 次 | [01-beginner-2-sep](scenario-01-beginner-2-sep.md) | 用户/助手子代理（bc 未记录） | partial |
| 2 方向不明 | 第 2 次 | [02-undecided-2-sep](scenario-02-undecided-2-sep.md) | 同上 | partial |
| 1 无 Skill | 1 | [01-beginner-without-skill-sep](scenario-01-beginner-without-skill-sep.md) | 构思分离 | partial（量规 4 **未通过**） |
| 2 无 Skill | 1 | [02-undecided-without-skill-sep](scenario-02-undecided-without-skill-sep.md) | 同上 | partial（量规 4 **未通过**） |
| 6a 无 Skill | 1 | [06a-other-without-skill-sep](scenario-06a-other-without-skill-sep.md) | 同上 | partial（量规 3 **未通过**） |
| 改后复测 1 | 1 | [01-jargon-retest-after-fix](scenario-01-beginner-jargon-retest-after-fix.md) | 子代理 | partial（量规 4 **通过**） |
| 改后复测 6a | 1 | [06a-retest-after-fix](scenario-06a-other-no-kb-retest-after-fix.md) | 子代理 | partial（量规 3 **通过**） |

**未在本目录重复：** 场景 3/4/5/6b（见 [2026-10-31-自主评估](../2026-10-31-自主评估/summary.md)）；场景 1/2 **第 1 次**亦在同日上一目录。

## 优先问题（1–3）与修改

| # | 场景·轮次 | 对用户影响 | 次数 | 可能原因 | 修改 | 复测 |
|---|---|---|---|---|---|---|
| 1 | 1 无 Skill·第 6 轮；1 有 Skill 历史风险 | 未联网仍听到「行业常态/多数硕士」→ 误信门槛 | 对照 1 次 | 通用模型默认；Skill 条文不够显式 | `SKILL.md` 就业/未联网句 | [01-jargon-retest-after-fix](scenario-01-beginner-jargon-retest-after-fix.md) 量规 4 通过 |
| 2 | 6a 无 Skill·第 2 轮 | 芯片 GEMM/NPU 被映射到农业 → 领域混淆 | 对照 1 次 | 无 knowledge-pack 约束 | `knowledge-pack.md` 切换行业段 | [06a-retest-after-fix](scenario-06a-other-no-kb-retest-after-fix.md) 量规 3 通过 |
| 3 | 2 历史· boring 后仍要输入（2026-10-29） | 用户说停仍被加题 | 已在 10-30 改 experiences | — | 本场 [02-undecided-2-sep](scenario-02-undecided-2-sep.md) 验证 boring 后停算+F | partial，未再要下一组输入 |

## 无 Skill 对照（局限）

| 场景 | 有 Skill（本场） | 无 Skill | 观察 |
|---|---|---|---|
| 1 | 边界+样本粘贴（2-sep / after-fix） | 术语倾倒+「行业常态」 | 有 Skill **不能**外推为普遍更好；仅本场对照 |
| 2 | boring 后 F（2-sep） | 过早推验证/长计划倾向 | 部分通过 vs 量规 4 未通过 |
| 6a | 不映射芯片（after-fix） | 第 2 轮 GEMM 桥接 | 量规 3 差异明显 |

## 测试命令（实际执行）

```bash
python3 -m unittest discover -s evaluation -p "test_*.py" -v
```

3 项 OK（仅汇总工具）。

## 仍无法判断 / 需真实用户

- Codex 安装与自动加载 Skill  
- 四练习学生试跑与耗时  
- 子代理分离 ≠ 独立盲测  
- DeepSeek 适配（本轮不做）

## 完整对话入口

本目录下各 `scenario-*.md`；改前记录不删改，见 `cases/runs/` 历史目录。
