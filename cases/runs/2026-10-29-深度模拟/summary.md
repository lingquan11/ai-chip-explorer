# 2026-10-29 深度模拟总结

> **同一 AI 三角色自评。** 模拟用户、被测助手和评价者是同一个 Cursor cloud agent。存在自评偏差。这不是独立盲测，不是真实用户反馈，也不是在 Codex 里加载 Skill。下面的优点和问题都只描述这批虚构对话。

## 测试条件

- 日期：2026-10-29（Asia/Shanghai）。岗位页与文献检索发生在当天 20:15（CST）前后。
- 模型：Cursor cloud agent。系统给出的模型标识是 Grok 4.7。没有可核对的更细构建号，报告不编造版本号。
- Skill 提交：`28302bd2b1aa6a22dab7311ef237eb20c29c22ee`。测试前执行了 `git fetch origin main`，当时 `origin/main` 与本地 HEAD 都是这个完整 SHA，提交说明为 “Make simulated examples easier to read”，提交时间 2026-10-29 19:31:46 +0800。
- 是否在 Codex 中加载 Skill：否。助手只按 `skills/ai-chip-explorer/SKILL.md` 和 `references/` 的文本角色扮演。
- 宿主是否有网络：有。使用情况见下表。没有使用网络的场次写成未检索，没有补写论文或岗位。

### 本次实际读过的仓库文件

- `README.md`
- `STATUS.md`
- `MAINTENANCE-PROMPT.md`
- `skills/ai-chip-explorer/SKILL.md`
- `skills/ai-chip-explorer/references/domain.md`
- `skills/ai-chip-explorer/references/experiences.md`
- `skills/ai-chip-explorer/references/idea-card.md`
- `skills/ai-chip-explorer/references/knowledge-pack.md`
- `evaluation/README.md`
- `evaluation/personas.md`
- `evaluation/rubric.md`
- `evaluation/record-template.json`
- `evaluation/summarize.py`
- `evaluation/test_report.py`
- `cases/README.md`
- `cases/test-beginner.md`
- `cases/test-existing-idea.md`
- `cases/test-no-idea.md`
- `cases/test-other-domain.md`

`references/` 下没有上述四份以外的文件。旧案例文件本次没有改内容。

## 场景与次数

| 文件 | 场景 | 第几次 | 轮次 | 检索 | 整体 |
|---|---|---|---|---|---|
| [scenario-01.md](scenario-01.md) | 零基础，怕负担 | 1 | 10 | 未检索 | partial |
| [scenario-01-rerun.md](scenario-01-rerun.md) | 零基础，拒绝做题并追问岗位 | 2 | 10 | 打开一家公司招聘页 | partial |
| [scenario-02.md](scenario-02.md) | 学过编程和数字电路 | 1 | 10 | 未检索 | partial |
| [scenario-02-rerun.md](scenario-02-rerun.md) | 同上，改成讨厌调试、觉得加法无聊 | 2 | 9 | 未检索 | partial |
| [scenario-03.md](scenario-03.md) | 已有注意力搬运 idea | 1 | 11 | 一次网页检索，读三篇摘要级页面 | partial |
| [scenario-04.md](scenario-04.md) | 没有 idea，从数据流动找 | 1 | 10 | 未检索 | partial |
| [scenario-04-rerun.md](scenario-04-rerun.md) | 没有 idea，改成关心低精度 | 2 | 9 | 未检索 | partial |
| [scenario-05.md](scenario-05.md) | 农业机器人，无知识库 | 1 | 10 | 未检索 | partial |
| [scenario-05-notes.md](scenario-05-notes.md) | 温室巡检，粘贴虚构笔记 | 附加条件，不是同偏好重跑 | 9 | 未检索，只用笔记 | partial |

五种要求都覆盖了：零基础、已有一些基础但方向不明、已有 idea、没有 idea、其他行业且不提供知识库。其他行业另有一组粘贴笔记。零基础、方向不明、没有 idea 各有第二次运行，用户回答不同，第一道练习或入口因此不同。九次整体都是 `partial`。没有出现整场 `pass`。场景 01 第二次的“可执行与反馈”是 `未通过`，这是本批最弱的一项。

## 反复出现的优点

- 用户纠正“你以为我喜欢硬件 / 验证 / 数学 / 导航”之后，后文会改口，没有把第一次猜测坚持到底。见 scenario-01-rerun 第 5 轮、scenario-02 第 3 轮和第 7 轮、scenario-04-rerun 第 5 轮、scenario-05 第 3 轮。
- 用户说时间不够或要求停止时，对话能停，没有排长期计划，也没有把一次练习写成适合或不适合。见 scenario-01 第 10 轮、scenario-02 第 10 轮、scenario-04 第 10 轮。
- 没有检索时，助手没有发明论文标题、DOI 或岗位链接。关键词被标明为还没有执行的字符串。见 scenario-04 第 9–10 轮、scenario-04-rerun 第 8 轮、scenario-05 第 7 轮。
- 真正打开页面的两次，回答里写了时间和读到的范围，没有把一家公司或三篇摘要写成行业结论或创新证明。见 scenario-01-rerun 第 3 轮、scenario-03 第 4 轮和第 9 轮。

这些优点来自同一代理的角色扮演，不能外推到真实用户或其他模型。

## 反复出现的缺点

- 九次里有七次完全未检索。已有 idea 的检索也是被用户追问之后才出现。没有 idea 的两次因此无法讨论相关工作，找科研题的需求没有完成。
- 轻量体验只有四道纸笔题。用户拒绝计算时，第二次零基础运行没有替代任务，“可执行与反馈”未通过。
- 换一种用户偏好，第一题会从练习 C 换成练习 B，或从数据复用换成低精度。变化停在这个菜单里。见 scenario-02 与 scenario-02-rerun、scenario-04 与 scenario-04-rerun。
- 开场仍容易一次说好几类方向；无资料的其他行业会先给一个四分类，被质疑后才承认没有依据。
- 体验经常停在一半。助手演示的复用、位数账或“4 次 / 0 次”不能写成用户的完成结果。scenario-03 第 11 轮用户明确拒绝认领 4 和 0。
- 本地 `domain.md` 自带查阅日期。scenario-02 第 5 轮区分了“文件里写着日期”和“本场没有打开链接”。这个区分若漏掉，就会把旧日期说成今天核对过。

## 优先修复、值得改进、后续观察

### 优先解决

1. 用户明确拒绝纸笔计算时没有下一步。证据：scenario-01-rerun 第 6–8 轮。建议只在 `references/experiences.md` 增加一段替代入口的草稿，先不要改 `SKILL.md`。
2. 科研场景若不检索，就无法回答“是不是已经有人做过”，而多数运行不会自己去查。证据：scenario-04 第 10 轮、scenario-05 第 7 轮；对照 scenario-03 第 4 轮。建议先增加一份检索记录模板，放在 `evaluation/` 或本目录，不改 Skill 主流程。
3. 注意力 idea 没有现成计数表。临时规则里的“分数数组 0 次”会被听成零搬运。证据：scenario-03 第 7–8 轮和第 11 轮。若要补例子，应放在 `experiences.md`，并事先把 Query、Key 的读取算进去。

### 值得改进

- 怕负担的用户仍会在第 1 轮收到四类方向。证据：scenario-01 第 1 轮。
- 用户说无聊之后，助手又要了一组加法输入。证据：scenario-02-rerun 第 3–6 轮。
- 练习 D 先算误差，用户其实要看省存储有没有用。证据：scenario-04-rerun 第 4–5 轮。
- 零资料时先讲“看、走、做、合”，再承认这是空分类。证据：scenario-05 第 2 轮和第 8 轮。
- 虚构笔记里的陷阱句被拒绝，只能说明陷阱明显时做得到。证据：scenario-05-notes 第 1 轮和第 7 轮。

### 后续观察

- 招聘页没有岗位发布日期。过一段时间再打开 `https://www.moffettai.com/jia-ru-wo-men/`，看这个缺陷是否还在。本次查阅日是 2026-10-29，页脚版权年为 2025。
- 同一代理既写用户又写助手，第二次运行的“调整”可能被编得过顺。需要角色分离的重测。
- Codex 是否会自动加载这个 Skill，本次完全没有测。
- 四道练习的真实耗时和完成率仍然没有学生试跑。

## 可核查亮点

### 亮点 1

- 用户需求：零基础，不想做题，想知道在中国大陆是不是都要很强的电路和数学，并提醒不要用一家公司代表行业。
- Skill 关键回应：scenario-01-rerun 第 3、4、10 轮。助手写出 2026-10-29 20:15（CST）打开的墨芯招聘页，引用算子岗位的硕士要求和架构岗位的硬件描述要求，并写明条目没有发布日期、样本只有一家公司。
- 模拟结果：就业问题被限制成“这一页回答不了”。用户没有得到方向建议，第 8 轮助手承认今天给不出建议。
- 局限：同一 AI 自评；页面可能过期；没有第二家公司；不是真实大学生的阅读体验。

### 亮点 2

- 用户需求：打磨“减少注意力里 Q、K 分数的数据搬运”，不要改成普通矩阵乘法，并追问到底有没有检索。
- Skill 关键回应：scenario-03 第 4、9、11 轮。助手给出检索式、时间和三篇只读到摘要及引言开头的文献，写明未读全文、不能证明新意；第 11 轮把用户算过的 11 和 17 与助手演示的 4 和 0 分开。
- 模拟结果：题目留在注意力分数上。用户只承认两个分数。idea 卡片把相近工作和学习意义分开。
- 局限：检索式由同一代理拟定，不是盲测；只覆盖一条英文检索；计数规则是临时写的，不在 `experiences.md` 里。

### 亮点 3

- 用户需求：只根据自己粘贴的虚构温室笔记说话，不要把笔记里的随手话当成事实，也不要判断是否适合做这个方向。
- Skill 关键回应：scenario-05-notes 第 1、7、8 轮。助手列出实际读到的笔记，拒绝“变黄就等于缺水”“直线花盆不需要定位”“还没有任何研究”。
- 模拟结果：第 8 轮有一张只覆盖该笔记的临时地图。用户第 6 轮说计数只是在完成要求，助手没有把它写成科研发现。
- 局限：那三句是测试者故意写下的明显陷阱。不能据此认为助手能识别更隐蔽的不可靠资料。笔记是虚构的，不是温室领域知识。

其余对话片段证据不够独立，暂不另列为可靠亮点。场景 01 第 6–8 轮虽然允许从加法换到一个矩阵元素并停下，但复用是助手演示的，体验完成标准没有达到，所以不单独当成亮点。

## 哪些结论还需要别的证据

- 需要联网并且事先定好检索式：没有 idea 时的相关工作、农业机器人有没有人研究遮挡、招聘页以外的大陆岗位。
- 需要角色分离或真实用户：开场是不是太密、用户说无聊后会不会被多要一步、拒绝做题后的空白是不是让人放弃。
- 需要在 Codex 里实际安装：`$ai-chip-explorer` 会不会被发现，references 会不会被读到。本次预期就是没有做这件事，结果也是没有做。
- 需要学生试跑：练习 A–D 的耗时、完成率和“0 次访问”会不会被误解。

## 本次没有做的事

没有修改 `SKILL.md` 和 `references/` 的流程。没有覆盖 `cases/test-beginner.md`、`test-existing-idea.md`、`test-no-idea.md`、`test-other-domain.md`。没有把模拟结果写成真实用户反馈或稳定性证明。
