# 大创全链路参考

Use this reference when a request involves more than one stage of a 大创 project, especially 全套材料、申报到结题、过程管理、答辩、成果包装, or 材料清单.

## Stage Map

| 阶段 | 目标 | 常见产物 |
|---|---|---|
| 选题策划 | 找到可申报、可完成、可展示的题目 | 题目清单、选题对比、可行性分析、创新点 |
| 申报/开题 | 把想法包装成学校表格能接受的项目 | 申报书、开题报告、技术路线、预算、进度表 |
| 执行过程 | 留下项目推进证据 | 月度计划、会议纪要、实验日志、调研记录、代码/设计记录 |
| 中期检查 | 证明项目按计划推进 | 中期报告、阶段数据、问题清单、调整方案 |
| 结题验收 | 证明项目完成并有成果 | 结题报告、测试数据、成果清单、经费总结、证明材料 |
| 答辩展示 | 把项目讲清楚、讲像样 | PPT提纲、讲稿、演示脚本、Q&A |
| 成果包装 | 让成果可被评审理解和归档 | 软著材料、专利交底书提纲、竞赛文案、论文/报告摘要 |
| 可选绘图 | 补充非证据类视觉材料 | 封面图、概念图、场景图、海报图、PPT背景图 |

## Full Package Outline

For a 全链路材料包, generate these sections by default:

1. 项目定位与推荐题目
2. 选题可行性与竞品/同类项目分析
3. 申报书/开题报告
4. 项目进度计划与团队分工
5. 过程管理材料模板
6. 中期报告
7. 结题报告
8. 成果包装材料
9. 答辩PPT提纲与讲稿
10. 证明材料与替换清单

## Topic Evaluation Table

Use this table when the user has multiple possible directions:

| 题目 | 应用价值 | 创新性 | 可行性 | 展示效果 | 风险 | 推荐指数 |
|---|---:|---:|---:|---:|---:|---:|
| 题目A | 4 | 4 | 5 | 4 | 2 | 4.4 |
| 题目B | 5 | 3 | 3 | 5 | 4 | 3.8 |

Scores are 1-5. Explain the recommendation briefly.

## Topic Pitfall Check

Use this checklist before recommending a topic:

| 维度 | 高风险表现 | 调整建议 |
|---|---|---|
| 题目范围 | 同时承诺平台、算法、硬件、产业化 | 缩到一个核心场景和一个可演示闭环 |
| 数据来源 | 需要大量真实用户或行业数据但没有渠道 | 改为小规模调研、公开数据、台架测试或仿真验证 |
| 成果落点 | 只写研究意义，没有可交付物 | 明确系统原型、测试报告、截图、视频、软著材料等 |
| 经费匹配 | 设备昂贵或测试成本超出项目级别 | 改用现有设备、开源硬件、仿真或租借方案 |
| 答辩风险 | 创新点像套话，无法回答同类系统差异 | 补充对比对象、差异点和可验证指标 |

## Reviewer Audit

When reviewing an existing draft, return findings in this shape:

| 问题位置 | 风险 | 修改建议 |
|---|---|---|
| 立项依据第X段 | 只讲政策背景，没有落到项目功能 | 增加具体应用场景、目标用户和系统模块 |
| 创新点 | 表述过大，像成果宣传 | 改成可验证的2-4个创新点 |
| 预期成果 | 声称获奖/授权但缺证明 | 改为拟形成/计划申请，并列证明材料 |

## AI-tone Reduction Checklist

Use this when the user asks for 降AI味、去模板化、像学生自己写的、自然一点:

- Delete or rewrite unsupported big claims.
- Replace abstract adjectives with implementation details.
- Keep 1-2 policy/background sentences, then quickly move to scene, method, and deliverables.
- Use modest verbs such as `拟实现`, `计划完成`, `初步验证`, `形成原型`, `整理报告`.
- Keep all simulated data and placeholder achievements visibly labeled.
- Do not add fake personal experience, fake interview details, fake teacher comments, or fake dates.

## Consistency Check

Before final packaging, compare these fields across 申报书、开题、中期、结题、PPT:

| 字段 | 检查内容 |
|---|---|
| 项目题目 | 是否前后一致，简称是否统一 |
| 成员与指导老师 | 姓名、学院、分工是否冲突 |
| 项目周期 | 月份、阶段任务和中期/结题时间是否匹配 |
| 经费预算 | 总额、分项、已用经费、结余是否能对上 |
| 研究内容 | 申报承诺和结题完成内容是否能解释差异 |
| 数据与成果 | 示例数据是否标注，真实成果是否有证明材料 |

## Process Evidence Templates

### Monthly Plan

| 月份 | 目标 | 具体任务 | 负责人 | 预期产物 | 验收方式 |
|---|---|---|---|---|---|
| 第1月 | 需求分析 | 文献调研、用户场景梳理 | 负责人 | 调研报告 | 导师检查 |

### Meeting Minutes

| 字段 | 内容 |
|---|---|
| 会议时间 | YYYY-MM-DD |
| 参会人员 | 成员姓名 |
| 本次议题 | 需求、算法、实验、报告等 |
| 已完成事项 | 使用真实进度填写 |
| 待解决问题 | 使用真实问题填写 |
| 下阶段任务 | 明确负责人和截止时间 |

### Experiment Log

| 字段 | 内容 |
|---|---|
| 实验编号 | EXP-001 |
| 实验目的 | 验证某模块性能 |
| 实验条件 | 场地、设备、版本、样本量 |
| 指标 | 准确率、耗时、误差、满意度等 |
| 原始记录 | 数据文件、截图、视频、日志路径 |
| 结论 | 仅基于真实数据填写 |

## Risk Register

| 风险 | 表现 | 影响 | 应对策略 |
|---|---|---|---|
| 技术难度过高 | 算法效果不稳定 | 影响结题演示 | 降低功能范围，保留核心闭环 |
| 设备不足 | 实机测试次数少 | 数据支撑不足 | 增加仿真验证和台架测试 |
| 数据质量不足 | 样本量少、噪声大 | 结果说服力不足 | 明确采集规范，补充对照实验 |
| 进度延误 | 开发和报告冲突 | 影响中期/结题 | 月度检查，拆分最低可交付版本 |
| 安全合规 | 飞行、用电、人体数据等限制 | 影响实验开展 | 使用封闭场地、模拟数据、匿名调研 |

## Achievement Packaging

### Software Copyright Placeholder

Use only as a writing template unless the user has a real work:

- 软件名称：XXXX系统V1.0
- 开发完成日期：YYYY-MM-DD
- 主要功能：数据采集、算法处理、可视化、报告导出
- 证明材料：源代码、操作说明、界面截图、测试记录
- 状态：拟申请/申请中/已授权，按真实情况填写

### Patent Disclosure Outline

- 技术领域
- 背景技术
- 发明内容
- 技术方案
- 有益效果
- 附图说明
- 具体实施方式
- 可替代方案

### Competition Entry Copy

- 作品名称
- 赛道匹配
- 痛点问题
- 技术方案
- 创新点
- 应用场景
- 实验验证
- 团队分工
- 商业化或推广设想

### Award Placeholder

Label this as `获奖情况（参考示例/占位示例）` unless verified:

| 奖项名称 | 等级 | 主办单位 | 获奖时间 | 作品名称 | 证明材料 |
|---|---|---|---|---|---|
| 第X届校级创新创业训练成果展 | 二等奖 | XX大学 | YYYY-MM | XXXX | 证书/公示截图 |

## Defense Package

### PPT Outline

1. 封面：项目名称、团队、指导教师
2. 背景痛点：场景、问题、需求
3. 项目目标：解决什么、做到什么程度
4. 技术路线：系统架构或流程图
5. 核心创新：2-4点即可
6. 实现过程：硬件、软件、算法、数据
7. 测试验证：实验设计、指标、结果
8. 成果展示：系统截图、实物、视频、成果清单
9. 不足与改进：诚实说明边界
10. 总结致谢

### Short Defense Script

Structure a 3-5 minute script as:

- 30s: 背景与问题
- 45s: 项目目标与方案
- 90s: 实现过程和创新点
- 60s: 测试结果和成果
- 30s: 不足、展望、致谢

### Q&A Bank

Include answers for:

- 你们的创新点在哪里？
- 与已有方案相比有什么优势？
- 数据是怎么来的？
- 项目中最难的部分是什么？
- 经费主要花在哪里？
- 如果继续做，下一步怎么改进？
- 成果是否真实完成，有哪些证明材料？

## Optional Image Generation

Generated visuals can improve PPT, posters, and cover pages, but they must not replace real evidence.

| 用途 | 推荐做法 | 禁止做法 |
|---|---|---|
| PPT封面 | 生成项目场景氛围图，标注为视觉背景 | 当作真实项目现场照片 |
| 项目海报 | 生成概念插图、用户场景、产品渲染风格图 | 伪造成已完成实物或获奖证明 |
| 架构说明 | 优先用 Mermaid / PlantUML / 手工流程图 | 用模糊插画替代关键技术路线 |
| 系统展示 | 优先抓真实系统截图 | 用 AI 图冒充真实界面截图 |
| 方案草图 | 标注 `概念示意图` 或 `占位示意图` | 暗示已完成硬件或现场部署 |

Prompt structure:

```text
项目类型：XXXX
应用场景：XXXX
画面主体：XXXX
技术元素：XXXX
用途：PPT封面 / 海报 / 概念示意图 / 答辩背景
风格：干净、现代、适合高校项目答辩，不要文字水印
真实性标注：概念示意图，不代表真实实验照片
```

API configuration is manual. Keep keys in environment variables or a local `.env` file, not in project materials.

## Acceptance Checklist

Before finalizing a full package, ensure it contains:

- A title and short project summary.
- Stage-specific reports with consistent project scope.
- Timeline, team division, budget, risks, and evidence list.
- Data tables labeled correctly if simulated.
- Achievement and award sections labeled correctly if placeholders.
- A replacement checklist for all real names, dates, data, certificates, and school-specific fields.
